# -*- coding: utf-8 -*-

import csv
import pickle
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu, spilu
from utils import *


class PPRBase(object):

    def __init__(self, jump_prob=0.05):
        self.alias = 'base'
        self.verbose = True
        raise NotImplementedError

    def pp(self, message, *args, **kwargs):
        if self.verbose:
            print('[{}] {}'.format(self.alias, message), *args, **kwargs)

    def preprocess(self, filepath):
        raise NotImplementedError

    def query(self, q):
        raise NotImplementedError

    def save(self, filepath):
        raise NotImplementedError

    def load(self, filepath):
        raise NotImplementedError


class PPRBear(PPRBase):

    def __init__(self, jump_prob=0.05, drop_tol=1e-8, k=None, greedy=True, verbose=False):
        """
        Computes PPR using BEAR with SlashBurn. `drop_tol` denotes approximation (set 0 for exact solution). Note that the approximation might return non-stochastic pagerank values. `k` and `greedy` are options for SlashBurn.

        Args:
            jump_prob (float): Jumping probability of PPR.
            drop_tol (float): Drops entries with absolute value lower than this value when computing inverse of LUs (H11, S from the paper).
            k (int): SlashBurn finds top-k hubs. There is a rule of thumb, so if you're not familiar with SlashBurn, then leave it to None.
            greedy (bool): Hub selection on SlashBurn. See SlashBurn for more details.
            verbose (bool): Prints step messages if True.
        """
        self.alias = 'bear'
        self.verbose = verbose
        self.pp("initializing")
        self.c = jump_prob
        self.d = 1 - self.c
        self.t = drop_tol
        self.k = k
        self.greedy = greedy
        self.exact = False

    def preprocess(self, filepath):
        """Remember: row-first ordered csv file only!"""
        self.pp("reading")
        self.node2index, H = read_matrix(
            filepath, d=-self.d, add_identity=True)
        self.n, _ = H.shape
        if self.t is None:
            self.t = np.power(self.n, -0.5)
        elif self.t == 0:
            self.exact = True
        if self.k is None:
            self.k = max(1, int(0.001 * self.n))
        self.pp("running slashburn")
        self.perm_H, wing = slashburn(H, self.k, self.greedy)
        self.body = self.n - wing
        self.pp("sorting H")
        H = reorder_matrix(H, self.perm_H)
        self.pp("partitioning H")
        H11, H12, H21, H22 = matrix_partition(H, self.body)
        del H
        H11 = H11.tocsc()
        self.pp("computing LU decomposition on H11")
        if self.exact:
            self.LU1 = splu(H11)
        else:
            self.LU1 = spilu(H11, drop_tol=self.t)
        del H11
        self.pp("computing LU1 solve")
        S = H22 - H21 @ self.LU1.solve(H12.toarray())
        S = coo_matrix(S)
        self.pp("sorting S")
        self.perm_S = degree_reverse_rank_perm(S)
        S = reorder_matrix(S, self.perm_S)
        self.H12 = reorder_matrix(H12, self.perm_S, fix_row=True)
        self.H21 = reorder_matrix(H21, self.perm_S, fix_col=True)
        S = S.tocsc()
        del H12, H21, H22
        self.pp("computing LU decomposition on S")
        if self.exact:
            self.LU2 = splu(S)
        else:
            self.LU2 = spilu(S, drop_tol=self.t)
        # issue: this approximation drops accuracy way too much! why?
        """
        if not self.exact:
            H12 = drop_tolerance(self.H12, self.t)
            del self.H12
            self.H12 = H12
            H21 = drop_tolerance(self.H21, self.t)
            del self.H21
            self.H21 = H21
        """
        del S

    def query(self, q):
        self.pp("sorting q")
        q = q / q.sum()
        q = reorder_vector(q, self.perm_H, reverse=True)
        q1, q2 = q[:self.body], q[self.body:]
        q2 = reorder_vector(q2, self.perm_S, reverse=True)
        self.pp("computing r2 with LU2 solve")
        r2 = self.c * self.LU2.solve(q2 - self.H21 @ self.LU1.solve(q1))
        self.pp("computing r1 with LU1 solve")
        r1 = self.LU1.solve(self.c * q1 - self.H12 @ r2)
        r2 = reorder_vector(r2, self.perm_S)
        r = np.concatenate((r1, r2))
        return reorder_vector(r, self.perm_H)

    def save(self, filepath):
        self.pp("saving")
        with open(filepath, 'wb') as file:
            pickle.dump((self.c, self.body, self.perm_H, self.perm_S, self.H12,
                         self.H21, serialize_slu(self.LU1), serialize_slu(self.LU2)), file)

    def load(self, filepath):
        self.pp("loading")
        # todo: recover SuperLU from serialized slu
        """
        with open(filepath, 'rb') as file:
            self.c, self.body, self.perm_H, self.perm_S, self.H12, self.H21, slu1, slu2 = pickle.load(file)
        """
        raise NotImplementedError
