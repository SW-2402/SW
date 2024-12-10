import numpy as np

def generate_temperature_data(samples=1000):
    """체온 데이터 생성 (더미)"""
    np.random.seed(0)
    time_steps = np.linspace(0, 100, samples)
    return 36.5 + 0.5 * np.sin(0.1 * time_steps) + 0.3 * np.random.randn(samples)

def generate_blood_pressure_data(samples=1000):
    """혈압 데이터 생성 (더미)"""
    np.random.seed(1)
    systolic = 120 + 10 * np.sin(0.1 * np.linspace(0, 100, samples)) + 5 * np.random.randn(samples)
    diastolic = 80 + 5 * np.sin(0.1 * np.linspace(0, 100, samples)) + 3 * np.random.randn(samples)
    # return np.stack((systolic, diastolic), axis=1)  # 수축기/이완기 압력
    return systolic - diastolic  # 이완기 - 수축기 편차로 혈압 판단

def generate_ecg_data(samples=1000):
    """심전도 데이터 생성 (더미)"""
    np.random.seed(2)
    return np.sin(0.2 * np.linspace(0, 100, samples)) + 0.1 * np.random.randn(samples)
