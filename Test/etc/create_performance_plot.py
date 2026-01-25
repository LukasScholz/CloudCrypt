import matplotlib.pyplot as plt
import pandas as pd

TESTRESULTSFILE = "Test/testresults.csv"

def creat_horizontal_bar_plot():

    test_case = []
    speed = []

    df = pd.read_csv(TESTRESULTSFILE).sort_values(by="Total Speed", ascending=True)
    for i, speedvalue in enumerate(df["Total Speed"]):
        testtype = df.iloc[i]["TestType"]
        os = df.iloc[i]["OS"]
        pyversion = df.iloc[i]["Python Version"]
        test_case.append(f"{testtype}_{os}_{pyversion}")
        speed.append(float(speedvalue[:-5])*1000)



    plt.barh(test_case, speed, color='lightgreen')
    plt.ylabel('Performance Test')
    plt.xlabel('Speed in MB/s')
    plt.title('Performance Test Comparison')
    plt.savefig("Test/performance_results.svg")


if __name__ == "__main__":
    creat_horizontal_bar_plot()