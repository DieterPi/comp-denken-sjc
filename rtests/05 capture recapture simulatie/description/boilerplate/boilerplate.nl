# Gegevens
N <- 1000
t <- 200
n <- 200

n_simulation <- 1000
s <- rbinom(n_simulation, size = n, prob = t / N)

N_estimated <- as.integer(t * n / s)

N_estimated
mean(N_estimated)

boxplot(N_estimated)
