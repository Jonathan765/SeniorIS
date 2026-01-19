from sklearn.model_selection import train_test_split

def client_server_split(X, y, test_size=0.3, random_state=42):
    X_client, X_server, y_client, y_server = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_client, X_server, y_client, y_server
