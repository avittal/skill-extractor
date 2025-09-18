import pandas as pd
#import re
from collections import Counter
import matplotlib.pyplot as plt



#job_descriptions = [
   # "Looking for Data Scientist skilled in Python, SQL, Machine Learning, AWS.",
    #"Hiring ML Engineer with TensorFlow, PyTorch, NLP, Docker."
#]

df = pd.read_csv('job_descriptions.csv')
df.head()
print(df.head())

skill_list = [
    "Python", "Java", "C++", "SQL", "R", "TensorFlow", "PyTorch",
    "Machine Learning", "Deep Learning", "AWS", "Docker", "Kubernetes",
    "JavaScript", "HTML", "CSS", "Scala", "Go", "Spark"
]

#def clean_text(text):
 #   text = re.sub(r'\n+', ' ', text)  # remove newlines
  #  text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
   # text = text.lower()
    #return text

#df['Cleaned_JD'] = df['JD_Text'].apply(clean_text)
#df.head()
#skills_list = [
 #   "python", "sql", "java", "c++", "machine learning",
  #  "deep learning", "nlp", "tensorflow", "pytorch",
   # "aws", "docker", "kubernetes", "excel", "tableau", "microservices"
#]
#def extract_skills(jd_text, skills_list):
#  extracted = [skill for skill in skills_list if #re.search(r'\b'+re.escape(skill)+r'\b', jd_text)]
#  return extracted

#df['Extracted_Skills'] = df['Cleaned_JD'].apply(lambda x: extract_skills(x, #skills_list))
#df.head()

#all_skills = [skill for sublist in df['Extracted_Skills'] for skill in sublist]
#skill_counts = Counter(all_skills)
#top_10_skills = skill_counts.most_common(10)
#top_10_skills

#skills, counts = zip(*top_10_skills)
#plt.figure(figsize=(10,6))
#plt.barh(skills, counts, color='skyblue')
#plt.xlabel("Frequency")
#plt.title("Top 10 Skills Across Job Descriptions")
#plt.gca().invert_yaxis()  # highest at top
#plt.show()

# Extract skills
all_skills = []
for jd in df["JD_Text"]:
    for skill in skill_list:
        if skill.lower() in jd.lower():
            all_skills.append(skill)

# Count frequency
skill_counts = Counter(all_skills).most_common(10)

# Show table
print("\nTop 10 Extracted Skills:")
for skill, count in skill_counts:
    print(f"{skill}: {count}")

# Convert to DataFrame for plotting
skills_df = pd.DataFrame.from_records(skill_counts, columns=["Skill", "Count"])

# Plot
plt.figure(figsize=(8,5))
plt.bar(skills_df["Skill"], skills_df["Count"], color="skyblue")
plt.title("Top 10 Skills from Job Descriptions")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save chart instead of showing
plt.savefig("top_skills.png")
print("\nChart saved as top_skills.png ✅ (check your Files tab)")


#jd_input = input("Paste Job Description: ")
#extracted = extract_skills(clean_text(jd_input), skills_list)
#print("Extracted Skills:", extracted)
