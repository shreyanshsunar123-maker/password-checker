Password Strength Checker (Python).

This repository contains a Python-based password strength evaluation tool.
The program analyzes a user-provided password and scores it based on multiple criteria including:
	•	length
	•	character diversity
	•	repeated-sequence detection
	•	dictionary word detection
	•	ASCII pattern repetition
	•	entropy estimation
The tool is written for learning, experimentation, and improving password-security awareness.


Features.

1. Length-based scoring.
Passwords receive higher scores the longer they are.
This reflects the exponential growth of search space with length.

2. Character-diversity checks.
The script evaluates whether the password contains:
	•	uppercase letters
	•	lowercase letters
	•	digits
	•	symbols
More diversity → higher difficulty to brute-force → higher score.

3. Repetition and pattern detection.
The checker detects:
	•	repeated characters (e.g., aaaaa, 22222)
	•	repeated chunks (e.g., abcabcabc, 123_123_123)
	•	obvious keyboard runs (optional)
This prevents users from choosing predictable structures.

4. Dictionary word detection.
The tool loads a small dictionary and penalizes passwords containing:
	•	common English words
	•	common names
	•	common passwords
	•	leetspeak variations (e.g., p@ssw0rd becomes “password”)
This helps mitigate targeted guessing and dictionary attacks.

5. Entropy estimation.
The program computes estimated Shannon entropy based on character-set size and password length:

H = L * log_2(N)
Where:
	•	L = length of the password
	•	N = number of possible symbols (based on characters used)
Entropy is reported to the user for educational purposes.


How It Works.
The script evaluates the password step-by-step and accumulates a final score.
It then classifies the password as:
	•	Very Weak
	•	Weak
	•	Moderate
	•	Strong
	•	Very Strong
This classification is based on empirical scoring thresholds.

Usage.
Run the script using Python:python3 Passcheck.py
Enter a password at the prompt.
The script will output:
	•	individual checks
	•	reasons for deductions
	•	total score
	•	estimated entropy
	•	final strength category

  
Dependencies.
This project uses only the Python Standard Library:
	•	re (regular expressions)
	•	string
	•	math
No external packages required.



Folder Structure.
PasswordChecker/
│── Passcheck.py
│── dictionary/
│     ├── common_words.txt
│     ├── names.txt
│     └── passwords.txt
│── README.md



License
This project is released under the MIT License.
You may modify, reuse, and distribute it freely as long as attribution is preserved.


Future Improvements (optional).
You may extend this tool with:
	•	GUI interface
	•	password-generation mode
	•	probabilistic Markov-model scoring
	•	zxcvbn-style scoring
	•	hash-based leak-checking
