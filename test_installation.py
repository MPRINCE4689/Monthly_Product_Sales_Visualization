# Test script to verify that all required libraries are installed correctly

try:
    import matplotlib.pyplot as plt
    print("✅ matplotlib imported successfully")

    import pandas as pd
    print("✅ pandas imported successfully")

    import numpy as np
    print("✅ numpy imported successfully")

    print("\n🎉 All libraries are installed correctly!")
    print("You're ready to run the visualization script!")

    # Test basic functionality
    print("\nTesting basic functionality...")

    # Create a simple test plot
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, 'bo-')
    plt.title('Test Plot - Installation Successful!')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True)
    plt.show()

    print("✅ Test plot created successfully!")

except ImportError as e:
    print(f"❌ Error importing library: {e}")
    print("Please install the missing library using:")
    print("pip install matplotlib pandas numpy")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
