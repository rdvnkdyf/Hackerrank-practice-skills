import sys
import numpy as np

# This function calculates the predicted battery life based on a linear regression model.
def predict_battery_life():
    """
    Reads training data, fits a linear regression model, and predicts
    battery life for a given charging time.
    """
    
    # 1. READ AND PROCESS THE TRAINING DATA
    # The new training data is now directly embedded in the code to ensure consistency.
    training_data_str = """
2.81,5.62
7.14,8.00
2.72,5.44
3.87,7.74
1.90,3.80
7.82,8.00
7.02,8.00
5.50,8.00
9.15,8.00
4.87,8.00
8.08,8.00
5.58,8.00
9.13,8.00
0.14,0.28
2.00,4.00
5.47,8.00
0.80,1.60
4.37,8.00
5.31,8.00
0.00,0.00
1.78,3.56
3.45,6.90
6.13,8.00
3.53,7.06
4.61,8.00
1.76,3.52
6.39,8.00
0.02,0.04
9.69,8.00
5.33,8.00
6.37,8.00
5.55,8.00
7.80,8.00
2.06,4.12
7.79,8.00
2.24,4.48
9.71,8.00
1.11,2.22
8.38,8.00
2.33,4.66
1.83,3.66
5.94,8.00
9.20,8.00
1.14,2.28
4.15,8.00
8.43,8.00
5.68,8.00
8.21,8.00
1.75,3.50
2.16,4.32
4.93,8.00
5.75,8.00
1.26,2.52
3.97,7.94
4.39,8.00
7.53,8.00
1.98,3.96
1.66,3.32
2.04,4.08
11.72,8.00
4.64,8.00
4.71,8.00
3.77,7.54
9.33,8.00
1.83,3.66
2.15,4.30
1.58,3.16
9.29,8.00
1.27,2.54
8.49,8.00
5.39,8.00
3.47,6.94
6.48,8.00
4.11,8.00
1.85,3.70
8.79,8.00
0.13,0.26
1.44,2.88
5.96,8.00
3.42,6.84
1.89,3.78
1.98,3.96
5.26,8.00
0.39,0.78
6.05,8.00
1.99,3.98
1.58,3.16
3.99,7.98
4.35,8.00
6.71,8.00
2.58,5.16
7.37,8.00
5.77,8.00
3.97,7.94
3.65,7.30
4.38,8.00
8.06,8.00
8.05,8.00
1.10,2.20
6.65,8.00
    """
    
    charging_times = []  # List to store charging times (X values)
    battery_lives = []   # List to store battery lives (Y values)
    
    # Process the new training data from the string
    for line in training_data_str.strip().split('\n'):
        try:
            charge_time, battery_life = map(float, line.strip().split(','))
            charging_times.append(charge_time)
            battery_lives.append(battery_life)
        except ValueError:
            continue
    
    # Filter data for training the linear regression model.
    # We only train on data points where charging time is > 1.0 and battery life is < 8.0.
    # This helps the model learn the slope before the battery life caps at 8.0.
    filtered_X = []
    filtered_Y = []
    for x, y in zip(charging_times, battery_lives):
        if x > 1.0 and y < 8.0:
            filtered_X.append(x)
            filtered_Y.append(y)

    X_train = np.array(filtered_X)
    Y_train = np.array(filtered_Y)

    # 2. TRAIN THE LINEAR REGRESSION MODEL on the filtered data
    if len(X_train) == 0:
        # Handle cases where there is not enough data to train a meaningful model
        # We can use a default slope or a different simple heuristic if needed.
        m, b = 0.0, 0.0
    else:
        # Calculate the mean of X_train and Y_train
        mean_X = np.mean(X_train)
        mean_Y = np.mean(Y_train)
        
        # Calculate the slope (m) and the y-intercept (b)
        numerator = np.sum((X_train - mean_X) * (Y_train - mean_Y))
        denominator = np.sum((X_train - mean_X)**2)
        
        if denominator == 0:
            m = 0.0
            b = 0.0
        else:
            m = numerator / denominator
            b = mean_Y - m * mean_X
    
    # 3. READ THE NEW INPUT AND MAKE A PREDICTION
    # Read a single charging time from standard input
    try:
        input_charging_time = float(sys.stdin.readline().strip())
    except (ValueError, IndexError):
        print("Error: Invalid input. Please provide a single number.")
        return

    # Use a two-tiered prediction strategy based on the input value.
    if input_charging_time <= 1.0:
        predicted_battery_life = input_charging_time * 2
    else:
        # Use the trained linear model and cap the maximum battery life at 8.0.
        predicted_battery_life = min(m * input_charging_time + b, 8.0)
    
    # 4. PRINT THE OUTPUT
    # The output should be a single number rounded to 2 decimal places
    print(f"{predicted_battery_life:.2f}")

# Call the main function to run the program
if __name__ == "__main__":
    predict_battery_life()