---
name: write-body-text
description: Guide for writing the main body text of the teaching materials. Use this skill whenever you are tasked with writing, editing, or generating explanatory text for the textbook/modules.
---

# Write Body Text Skill

Whenever you write, rewrite, or edit the body text for this educational project, you MUST adhere to the following guidelines:

## 1. Language and Tone

- **Bahasa Indonesia**: Always write the body text in Indonesian.
- **Easy and Accessible Language**: Use simple, straightforward language ("bahasa yang mudah dipahami" or "sederhana"). Avoid overly academic, rigid, or convoluted phrasing. The priority is clarity and ease of understanding for students.
- **Engaging Tone**: Write in an engaging and conversational tone suitable for teaching material. Imagine you are explaining the concepts directly to a class of students.

## 2. Emphasizing Key Concepts

- **Bold Key Points**: Bold important terms, core ideas, and key takeaways (`**text**`). Because this material is intended to be used and read in a classroom setting, bolding helps students quickly scan and identify the most crucial pieces of information.
  - Good Example:
    Analisis statistika inferensial dengan uji hipotesis parameter digunakan untuk **memperkirakan nilai dari parameter** melalui **pengujian hipotesis nilai sebuah parameter** berdasarkan informasi yang diperoleh dari sampel, atau seperti yang telah kita pelajari, disebut **statistik** **(**[Healey 2021](http://127.0.0.1:4321/analisis-statistik-multivariat-interdependensi.html#ref-healey2021statistics)). Hipotesis sendiri dapat dipahami sebagai **dugaan awal mengenai suatu kondisi, nilai, atau keadaan parameter** . Dalam metode ilmiah, hipotesis berasal dari teori, penelitian sebelumnya, atau klaim tertentu yang ingin diuji **(**[Ewing and Park 2020](http://127.0.0.1:4321/analisis-statistik-multivariat-interdependensi.html#ref-ewing2020basic); [Healey 2021](http://127.0.0.1:4321/analisis-statistik-multivariat-interdependensi.html#ref-healey2021statistics)).
- **Visual Structure**: Use bullet points or short paragraphs where appropriate to break down complex ideas into digestible pieces. Avoid massive walls of text.

## 3. Contextual Understanding

- Keep explanations efficient but thorough enough to grasp the foundation of the topic.
- When explaining mathematical or statistical concepts, prioritize intuition and real-world logic over pure abstraction.

## 4. Formatting

- Give one space between a line and first bullet point to avoid misrendering of the bullet point by knitr
  - Good:

    ```markdown
    Contoh nama kota:

    - Lisbon
    - Paris
    - Magelang
    ```

  - Avoid:

    ```markdown
    Contoh nama kota:

    - Lisbon
    - Paris
    - Magelang
    ```
