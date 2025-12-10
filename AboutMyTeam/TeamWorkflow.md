# Team Workflow

## Team Members (สมาชิกและหน้าที่)
- **Member 1 (Worachat):** สร้าง Repo และโฟลเดอร์โครงสร้าง, เขียน Quick Sort **และเขียน Main Program เพื่อรวบรวมและทดสอบระบบ**
- **Member 2 (Krit):** เขียนและทดสอบ algorithm Bubble Sort

## Workflow Process (ขั้นตอนการทำงาน)
1. **Initial Setup:** Member 1 (Worachat) สร้าง Branch ส่วนตัว, สร้างโฟลเดอร์และไฟล์ที่จำเป็น (AboutMyTeam, Project, TeamWorkflow.md) พร้อมเขียนโค้ด Quick Sort **และ Main Program** ส่งขึ้น Main Branch
2. **Pull & Branch:** Member 2 (Krit) ต้องทำการ `git pull origin main` เพื่อดึงงานล่าสุดก่อน แล้วสร้าง Branch ส่วนตัว (`git checkout -b ชื่อ_รหัส`)
3. **Implementation:**
   - Member 2 (Krit) เขียนแนะนำตัวเองใน `AboutMyTeam/Krit_374-2.md` และเขียนโค้ด algorithm ใน `Project/bubble_sort.py`
4. **Merge & Push:** เมื่อเขียนและทดสอบเสร็จ ให้ Merge Branch ของตัวเองเข้ากับ Main (`git merge ...`) แล้ว Push ขึ้น GitHub
5. **Final Check:** ช่วยกันตรวจสอบความถูกต้องบน GitHub และแก้ไข Conflict ร่วมกัน