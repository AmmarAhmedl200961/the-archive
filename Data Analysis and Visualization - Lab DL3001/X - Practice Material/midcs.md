---
header-includes:
  - \usepackage[margin=1in]{geometry}
  - \usepackage{fancyvrb}
  - \usepackage{color}
  - \usepackage{framed}
  - \usepackage{multicol}
  - \usepackage{hyperref}
  - \usepackage{listings}
  - \definecolor{shadecolor}{rgb}{0.9,0.9,0.9}
  - \lstset{
      basicstyle=\ttfamily,
      breaklines=true,
      backgroundcolor=\color{shadecolor},
      frame=single,
      rulecolor=\color{shadecolor},
      xleftmargin=0.5cm,
      xrightmargin=0.5cm
    }
---

\begin{multicols}{2}

DataFrame Basics:
  \begin{lstlisting}
  df.head(), df.tail()  # first & last 5 rows
  df.describe(), df.info(), df.shape  # Summary
  df.isnull().sum()  # Missing values
  df.iloc[0], df.iloc[:, 0]  # Row, column by index
  df.loc[df['c'] > 10]  # Conditional
  df.groupby('c').mean()  # Groupby
  \end{lstlisting}

Array Creation:
  \begin{lstlisting}
  np.array([1, 2, 3, 4])
  np.zeros((3, 3))  # 3x3 array of zeros
  np.ones((2, 2))  # 2x2 array of ones
  np.mean(arr), np.median(arr)  # Statistics
  np.sum(arr), np.dot(arr1, arr2)  # Sum Dot
  \end{lstlisting}

Basic Usage:
  \begin{lstlisting}
  requests.get('https://example.com').status_code  # HTTP status code
  html = requests.get('https://example.com').text
  soup = BeautifulSoup(html, 'html.parser')
  soup.find('a')  # Find first `<a>` tag
  soup.find_all('div', class_='class_name') # Find all tags with class 'class_name'
  soup.find_all('p')[2].get_text()  # Get text of third `<p>` tag
  soup.find_all(id='third')  # Find all tags with id 'third'
  \end{lstlisting}

Navigating the HTML:
  \begin{lstlisting}
  tag = soup.find('p')  # Get the first `<p>` tag
  tag.get_text()  # Extract text inside tag
  tag['href']  # Access tag attribute
  \end{lstlisting}

Univariate and Bivariate:
  \begin{lstlisting}
  sns.distplot(df['c'])  # Histogram single column
  sns.countplot, sns.barplot, sns.boxplot(x='col1', data=df)
  sns.pairplot(df)  # Pairplot
  sns.heatmap(df.corr(), annot=True)  # Heatmap
  sns.scatterplot(x='col1', y='col2', data=df)
  \end{lstlisting}


Outlier Removal (IQR):
  \begin{lstlisting}
  q1 = df['c'].quantile(0.25)
  q3 = df['c'].quantile(0.75)
  iqr = q3 - q1
  df_cleaned = df[(df['c'] >= q1 - 1.5*iqr) & (df['c'] <= q3 + 1.5*iqr)]
  \end{lstlisting}

Feature Engineering:
  \begin{lstlisting}
  df['new_c'] = df['c1'] * df['c2']
  pd.get_dummies(df, columns=['c'])  # Encoding
  \end{lstlisting}

Scaling Features:
  \begin{lstlisting}
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  df[['c1', 'c2']] = scaler.fit_transform(df[['c1', 'c2']])
  \end{lstlisting}

Encoding Categorical Variables:
  \begin{lstlisting}
  pd.get_dummies(df, columns=['c'])  # One-hot encoding
  from sklearn.preprocessing import LabelEncoder
  le = LabelEncoder()
  df['c'] = le.fit_transform(df['c'])
  \end{lstlisting}

OpenCV Basics:
  \begin{lstlisting}
  img = cv2.imread('img.jpg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  resized = cv2.resize(img, (width, height))
  \end{lstlisting}

Blur, Canny and Image Translation and Rotation:
  \begin{lstlisting}
  (h, w) = img.shape[:2]
  center = (w // 2, h // 2)
  blurred = cv2.GaussianBlur(img, (kx, ky), 0)
  edges = cv2.Canny(gray, upper, lower)
  M_rot = cv2.getRotationMatrix2D(center, angle, 1.0)  # Rotation
  rotated = cv2.warpAffine(img, M_rot, (w, h))
  cv2.circle(img, (x, y), radius, (b, g, r), thickness)  # Circle
  \end{lstlisting}

NLP Text Preprocessing, Tokenization, Stopwords, TF-IDF and Cosine Similarity:
  \begin{lstlisting}
  stop_words = set(nltk.corpus.stopwords.words('english'))
  tokens = nltk.tokenize.word_tokenize(text)
  filtered = [w for w in tokens if w not in stop_words]
  from sklearn.feature_extraction.text import CountVectorizer
  vectorizer = CountVectorizer()
  X = vectorizer.fit_transform(['sample text', 'another text'])
  tfidf = TfidfVectorizer()
  X = tfidf.fit_transform(texts)
  cosine_sim = cosine_similarity(X)
  \end{lstlisting}

Naive Bayes on Text:
  \begin{lstlisting}
  from sklearn.naive_bayes import MultinomialNB
  model = MultinomialNB()
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)
  \end{lstlisting}

\end{multicols}