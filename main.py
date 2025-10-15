def greet(name="World"):
    """
    ฟังก์ชันสำหรับแสดงคำทักทาย
    """
    message = f"Hello, {name}! ยินดีต้อนรับสู่โปรเจกต์ Python ที่ใช้ Git/GitHub"
    print(message)
    return message

if __name__ == "__main__":
    greet("Developer")

# เพิ่มฟังก์ชันใหม่สำหรับการแก้ไขเพิ่มเติม
def calculate_sum(a, b):
    """
    ฟังก์ชันสำหรับคำนวณผลรวม
    """
    return a + b

# ทดสอบฟังก์ชันใหม่
# print(f"The sum of 5 and 3 is: {calculate_sum(5, 3)}")