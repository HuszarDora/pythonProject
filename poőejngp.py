import numpy as np

#step1 kovariancia mátrix számítása


def calc_covar(corr, szoras_a, szoras_b):
    cov_matrix = np.zeros((2, 2))
    cov_matrix[0, 0] = szoras_a ** 2
    cov_matrix[1, 1] = szoras_b ** 2
    cov_matrix[1, 0] = corr * szoras_a * szoras_b
    cov_matrix[0, 1] = corr * szoras_a * szoras_b
    return cov_matrix


#print(calc_covar(0.1, 0.14, 0.05))
#step2 hozamok generálása


def sim_portfolio(mean, cov_matrix, size):
    sim_returns = np.random.multivariate_normal(mean, cov_matrix, size)
    return sim_returns


#print(np.mean(sim_portfolio([0.3, 0.7], [[0.1, 0.05], [0.05, 0.1]], 1000), axis=0))
#print(np.cov(sim_portfolio([0.3, 0.7], [[0.1, 0.05], [0.05, 0.1]], 1000).T))


def calc_portfolio_return(weight_1, weight_2, return_1, return_2):
    return weight_1 * return_1 + weight_2 * return_2
