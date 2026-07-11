# شرح تقسيمة ملفات LEXORA Frontend Pro

## أهم فكرة

الفرونت معمول بـ React + Vite، ومقسّم بطريقة مرتبة عشان تعرف تعدّل بسهولة.

## التشغيل

```cmd
cd /d "D:\DEPI project\lexora-frontend-pro"
npm install --registry=https://registry.npmjs.org/
copy .env.example .env
npm run dev
```

## الملفات الرئيسية

### `src/App.jsx`
مسؤول عن التنقل بين الصفحات باستخدام hash routes:

- Home
- Generate
- Workflow
- Team

### `src/main.jsx`
نقطة تشغيل React.

### `src/styles/globals.css`
أهم ملف للشكل والتصميم كله. لو عايز تغير الألوان أو حجم الكروت أو شكل الصفحة غالبًا هتعدل هنا.

---

## فولدر `pages`

### `HomePage.jsx`
صفحة البداية: Hero section، preview، أنواع المحتوى، وأمثلة prompts.

### `GeneratePage.jsx`
أهم صفحة. فيها الفورم، progress، والنتيجة.

### `AboutPage.jsx`
بتشرح workflow بتاع المشروع: Outline Agent, Search Agent, Router Agent, Writer Agent, Critique Agent.

### `TeamPage.jsx`
صفحة الفريق.

---

## فولدر `components/common`

### `Navbar.jsx`
الشريط العلوي واللوجو النصي.

### `Footer.jsx`
الفوتر.

### `Button.jsx`
زرار reusable.

### `Card.jsx`
كارت reusable.

### `EmptyState.jsx`
الشكل اللي بيظهر قبل ما يكون فيه generated result.

---

## فولدر `components/generator`

### `GenerateForm.jsx`
الفورم الأساسي: Topic, Content Type, Tone.

### `AdvancedOptions.jsx`
الاختيارات الإضافية: Audience, Max Tokens, Brief, Reference Text.

### `ProgressPanel.jsx`
يعرض حالة الـ job والـ progress.

### `ResultPanel.jsx`
يعرض الناتج، وزرار Copy و Download و Clear.

---

## فولدر `services`

### `apiClient.js`
بيقرأ `VITE_API_BASE_URL` من `.env` وبيعمل requests للباك إند.

### `generationApi.js`
فيه الدوال اللي بتكلم endpoints:

- generate
- job status
- job result

---

## فولدر `hooks`

### `useGenerationJob.js`
ده أهم logic في الفرونت:

1. يبعت request للباك إند.
2. ياخد job_id.
3. يعمل polling.
4. يجيب النتيجة النهائية.
5. يتعامل مع errors.

---

## فولدر `constants`

### `contentOptions.js`
هنا تعدل:

- Content types
- Tone options
- Token options
- Cards المعروضة في Home

### `team.js`
هنا تعدل أسماء التيم.

### `appInfo.js`
اسم ووصف المشروع.

---

## ملاحظات مهمة

- اختيار `None` في dropdown مش بيتبعت للباك إند.
- الـ backend هو اللي بيستخدم default values.
- الفرونت لا يحتوي على login أو history أو debug page.
