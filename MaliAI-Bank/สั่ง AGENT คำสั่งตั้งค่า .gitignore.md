หัวข้อ: ขั้นตอนการตั้งค่า .gitignore เพื่อความปลอดภัยของ Repository
1. เป้าหมาย (Objective):
สร้างไฟล์ .gitignore เพื่อคัดกรองไม่ให้ไฟล์ที่มีข้อมูลสำคัญ (Sensitive Data) หรือไฟล์ขยะ (System Files) ถูกบันทึกเข้าสู่ระบบ Git (Commit/Push) เพื่อป้องกันความปลอดภัยของบัญชีและประวัติของโปรเจกต์
2. ขั้นตอนการดำเนินการ (Instructions for Agent):
สร้างไฟล์ชื่อ: .gitignore (ต้องมีจุดนำหน้าและไม่มีนามสกุลไฟล์) ไว้ที่ Root Directory ของโปรเจกต์
ระบุรายการไฟล์ที่ต้องยกเว้น (Standard Exclusion):
ไฟล์ Environment (.env, .env.local, .env.auth)
ไฟล์เก็บกุญแจรหัสผ่าน (*.pem, *.key, *.p12)
โฟลเดอร์ Library (node_modules/, vendor/, pycache/)
ไฟล์ระบบ (DS_Store, Thumbs.db, .vscode/, .idea/)
สร้างไฟล์ตัวอย่าง (Best Practice):
สร้างไฟล์ชื่อ .env.example เพื่อเก็บโครงสร้างชื่อตัวแปร (แต่ไม่ใส่ค่าจริง) เพื่อให้คนอื่นในทีมรู้ว่าต้องตั้งค่าตัวแปรอะไรบ้าง
3. รายการเนื้อหาภายในไฟล์ .gitignore (Template Content):
# --- Security & Credentials ---
.env
.env.local
.env.*
*.pem
*.key
credentials.json
auth.json

# --- Dependency Folders ---
node_modules/
vendor/
bin/
obj/
__pycache__/

# --- OS & IDE Files ---
.DS_Store
Thumbs.db
.vscode/
.idea/
*.swp

# --- Logs & Temp ---
*.log
logs/
tmp/
dist/
build/
