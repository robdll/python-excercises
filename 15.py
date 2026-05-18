from scipy.stats import binom, geom

# Un medico visita pazienti durante la giornata. 
# Ogni paziente ha il 15% di probabilità di avere bisogno di un esame urgente, indipendentemente dagli altri.
# Parte A:
# Sia X il numero di pazienti visitati fino al primo 
# che necessita di un esame urgente (incluso).
# Che distribuzione segue X? Risposta: Geometrica
X = geom(.15)
# Calcola E(X) e Var(X)
#E(X) = 1/h = 1/.15 = 6.67
#SOL: Var(X) = 0.85 / 0.0225 = 37.8
print(X.mean())
print(X.var())
# Calcola P(X=5)
#SOL: P(X=5) = .85^4 * .15 = .08
print(X.pmf(5))
# Calcola P(X>3)
#SOL: P(X>3) = .85^3 = 0.61
print(1 - X.cdf(3))

# Parte B:
# In una mattinata il medico visita 12 pazienti. 
# Sia Y il numero di pazienti che necessitano di un esame urgente.
# Che distribuzione segue Y? Binomiale
Y = binom(12,.15)
# Calcola E(Y) e Var(Y)
#SOL: E(Y) = 12 * .15 = 1.8
#SOL: Var(Y) = 12 * .15 * .85 = 1.53
print(Y.mean())
print(Y.var())
# Calcola P(Y=2)
#SOL: P(Y=2) = C(12,2) * .15^2 * .85^10 = .29
print(Y.pmf(2))
# Calcola P(Y>=1) — almeno un paziente urgente
#SOL: P(Y>=1) = 1 - P(Y=0) = 1 - .142 = .858
print(1 - Y.cdf(0))
