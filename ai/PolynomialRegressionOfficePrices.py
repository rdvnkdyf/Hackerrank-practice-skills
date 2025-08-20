import numpy as np

def solve():
    f, n = map(int, input().split())

    training_data = []
    for _ in range(n):
        training_data.append(list(map(float, input().split())))

    training_data = np.array(training_data)

    X_train = training_data[:, :f]
    y_train = training_data[:, f]

    poly_features = []
    for i in range(f):
        
        poly_features.append((X_train[:, i]**2).reshape(-1, 1))
        for j in range(i + 1, f):
            
            poly_features.append((X_train[:, i] * X_train[:, j]).reshape(-1, 1))
    
    poly_X_train = np.hstack([X_train] + poly_features)
    
    X_train_augmented = np.hstack([np.ones((n, 1)), poly_X_train])
    
    theta = np.linalg.inv(X_train_augmented.T @ X_train_augmented) @ X_train_augmented.T @ y_train
    
    t = int(input())

    for _ in range(t):
        test_features = np.array(list(map(float, input().split())))

        poly_test_features = []
        for i in range(f):
            poly_test_features.append(test_features[i]**2)
            for j in range(i + 1, f):
                poly_test_features.append(test_features[i] * test_features[j])
        
        test_features_expanded = np.hstack([test_features] + poly_test_features)

        X_test_augmented = np.hstack([[1], test_features_expanded])
        
        predicted_price = X_test_augmented @ theta

        print(f"{predicted_price:.2f}")

solve()