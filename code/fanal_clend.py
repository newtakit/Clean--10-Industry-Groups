import pandas as pd

file_path = r'C:/Users/newta/OneDrive/Desktop/new-git-test/Clean--10-Industry-Groups/data10/fac-10scurve.csv'

def A1(file_path):
    df = pd.read_csv(file_path)

    df.columns = df.columns.str.replace(' ', '')
    df['คนงานรวม'] = pd.to_numeric(df['คนงานรวม'], errors='coerce').fillna(0).astype(int)
    df['แรงม้า'] = pd.to_numeric(df['แรงม้า'], errors='coerce').fillna(0).astype(float)

    # ลบโรงงานที่ไม่มีชื่อออก
    df = df.dropna(subset=['ชื่อโรงงาน'])

    # บันทึกไฟล์ CSV ที่สะอาดแล้ว
    output_file = 'fac-10scurve_cleaned.csv'
    df.to_csv(output_file, index=False)

    print(f"บันทึกไฟล์ CSV เรียบร้อยแล้ว: {output_file}")
    return df

# ใช้งานฟังก์ชัน A1
cleaned_df = A1(file_path)