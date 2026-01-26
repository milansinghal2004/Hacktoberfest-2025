import numpy as np

def linear_regression(X, y):
    if len(X) != len(y):
        raise ValueError("X and y must have the same length.")
    
    n = len(X)
    mean_x, mean_y = np.mean(X), np.mean(y)
    
    numerator = np.sum((X - mean_x) * (y - mean_y))
    denominator = np.sum((X - mean_x) ** 2)
    
    if denominator == 0:
        raise ValueError("Variance of X is zero. Cannot fit a line.")
    
    m = numerator / denominator
    
    c = mean_y - m * mean_x
    
    return m, c
def predict(X, m, c):
    return m * X + c
def r2_score(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    return 1 - (ss_residual / ss_total)
if __name__ == "__main__":
    np.random.seed(42)
    X = np.linspace(0, 10, 50)
    y = 3.5 * X + 5 + np.random.randn(50) * 2
    m, c = linear_regression(X, y)
    print(f"Slope (m): {m:.4f}")
    print(f"Intercept (c): {c:.4f}")
    y_pred = predict(X, m, c)
    score = r2_score(y, y_pred)
    print(f"R² Score: {score:.4f}")
    try:
        import matplotlib.pyplot as plt
        plt.scatter(X, y, label="Data Points")
        plt.plot(X, y_pred, color="red", label="Best Fit Line")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.show()
    except ImportError:
        print("matplotlib not installed. Skipping plot.")
