import joblib
file_path = r"D:\Infosys internship\AI-Powered-Loan-Eligibility-Advisor\model.pkl"

with open(file_path, "rb") as f:
    content = f.read(20)
print(content)
model_path = r"D:\Infosys internship\AI-Powered-Loan-Eligibility-Advisor\model.pkl"
model = joblib.load(model_path)
print("✅ Model loaded successfully!")
