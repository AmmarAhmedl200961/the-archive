# the-archive

Welcome! This repository is **the-archive** – a complete dump of the resources I personally used during my university years.

The goal is to:

- Preserve **everything I studied from** in one place.
- Give **juniors a fun, open archive** to explore past course material.
- Keep my notes, slides, labs, and other resources under **version control** instead of random folders.

This is **not** an official course mirror and has no affiliation with the university or any instructor.

---

## What’s Included

I’ve tried to include **every resource I actually used**, including (but not limited to):

- Lecture slides and handwritten/typed notes  
- Handouts, reference PDFs, and textbooks/extracts  
- Assignments, quizzes, and exams (plus solutions, where available)  
- Lab sheets, lab code, datasets, and supporting files  
- Google Classroom exports and Google Drive materials  
- Any extra materials that helped me understand the content

If I used it to study, revise, or practice, I tried to **put it in here**.

> **Important:** Some content may appear more than once (duplicates) because of repeated courses, multiple exports, or overlapping resources. I prefer **completeness over minimalism**.

---

## Duplicate / Repeated Courses

During my degree:

- Some courses were **repeated or retaken**.
- Some courses appeared as **multiple Google Classroom instances** across semesters.
- Some files were re-uploaded or re-shared in different places.

Because this archive aims to be a **full snapshot** of what I had access to:

- Not every “repeat” is explicitly marked as “this is a repeat of X”.
- You may see **the same or very similar material multiple times**.
- That’s intentional: this is how the data originally existed in my storage and exports.

So if you notice double material:

> That’s expected – it reflects multiple runs/versions of a course, not an error in the-archive.

---

## Folder Structure & Reachability

The structure is designed for **reachability**, so you can quickly get to what you care about.

A typical layout looks like:

- `Semester X/`
  - `Course - Course Name/`
    - `00 - Info/`  
      - syllabus, grading policies, general course info, exports (e.g. Classroom snapshots)
    - `01 - Lectures/`
    - `02 - Labs/`
    - `03 - Quizzes/`
    - `04 - Midterms/`
    - `05 - Final/`
    - `99 - Misc/`

Inside those, individual events often get their own folder, for example:

- `Quiz 01/`
- `Midterm 1 Solution/`
- `Lab 03 - Topic Name/`

Whenever an item is clearly a quiz, lab, midterm solution, etc., it’s given a **dedicated folder** so it’s easy to navigate.

---

## For Juniors: How to Use this Archive

This archive is mainly for:

- **Exploration** – see how courses were structured and what kind of material showed up.
- **Practice** – reuse old quizzes, assignments, and exams as practice questions.
- **Orientation** – understand the level, style, and expectations of courses before you take them.
- **Inspiration** – see how labs, projects, and solutions were organized.

Please use this responsibly:

- Respect your university’s **academic integrity policies**.
- Don’t use this to **cheat in active courses** (copying solutions, handing in old code, etc.).
- Use it as:
  - Extra reference material  
  - A practice bank  
  - A guide to what to expect  

Have fun exploring the-archive and learning from it.

---

## Git Workflow (How I Keep `the-archive` Synced)

I’m managing `the-archive` **locally on Windows** using Git and pushing to GitHub. This ensures:

- Every change (added files, reorganized folders, cleaned-up structure) is **tracked over days/weeks**.
- I can safely **delete old manual folders** once I confirm everything is pushed to GitHub.
- The repo becomes my **single source of truth**.

### 1. One-Time Setup (after creating the repo on GitHub)

On GitHub (web):

1. Create a new repository named **`the-archive`** under your account.
2. You can leave it empty or let GitHub create a default README (you can overwrite it later).

On Windows (Terminal / PowerShell / Git Bash), assuming your archive folder is ready:

```bash
# Go to the folder that contains your archive
cd "C:\path\to\the-archive"

# Initialize Git in this folder
git init

# Add the remote pointing to your GitHub repo
git remote add origin https://github.com/AmmarAhmedl200961/the-archive.git
```

If you want to confirm the remote:

```bash
git remote -v
```

### 2. First Commit and Push

```bash
# See current status
git status

# Add all files in the-archive
git add .

# Create the initial commit
git commit -m "Initial import of university archive"

# Make sure the main branch is called 'main' and push it
git branch -M main
git push -u origin main
```

Then, open [the repository on GitHub](https://github.com/AmmarAhmedl200961/the-archive) and confirm:

- The folder structure is there.
- `README.md` renders correctly.
- File counts look reasonable.

Only after this verification should you start deleting any **separate manual copies** of your old archive.

---

## 3. Ongoing Workflow (Daily / Whenever You Change Stuff)

Whenever you:

- Add new files or courses
- Rearrange folders
- Clean duplicates
- Update notes

From your repo folder:

```bash
cd "C:\path\to\the-archive"

# See what changed
git status

# Optional: see the actual text differences for tracked files
git diff
```

If everything looks good:

```bash
# Stage all new/modified/deleted files
git add .

# Commit with a message describing the change
git commit -m "Reorganize labs and add missing quiz solutions"

# Push to GitHub
git push
```

Do this regularly so:

- Every step of your reorganization is saved.
- You can roll back if something goes wrong.
- The GitHub copy stays current.

---

## 4. Safely Deleting Old Manual Archives

You can safely delete your old scattered notes/slides folders **only after**:

1. Those files/folders have been moved into `the-archive` (this repo’s folder).
2. You’ve run `git add .`, `git commit`, and `git push`.
3. You’ve checked GitHub and confirmed the content is visible and correct.

If unsure, keep old folders for a bit longer until you’re confident everything is inside `the-archive` and backed up remotely.

---

## Contributions & Feedback

If you’re using this archive and you:

- Notice broken structure or obvious mislabels
- Have better organization ideas
- Want to contribute additional resources (that are allowed to be shared)

you can open issues or pull requests on GitHub.

The goal is that `the-archive` stays:

- **Useful** to juniors and others
- **Searchable** and easy to navigate
- **Honest** to what I actually used while studying

Enjoy exploring `the-archive` and make your own archives too.