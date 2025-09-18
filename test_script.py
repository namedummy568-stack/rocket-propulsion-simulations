def thrust_vectoring_test():
    # Simulate thrust vectoring test
    stability_threshold = 0.5
    current_instability = 0.7 # Simulate a failure

    if current_instability > stability_threshold:
        raise ValueError("Stability threshold exceeded")

    print("Thrust vectoring test passed.")

if __name__ == "__main__":
    try:
        thrust_vectoring_test()
    except ValueError as e:
        print(f"Test failed: {e}")
