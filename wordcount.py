def count_words(file_path):
	# Initialize the hashmap to store word counts
	word_counts = {}
	total_words = 0
	
	# Read the file
	with open(file_path, 'r') as file:
		for line in file:
			# Split the line into words
			words = line.split()
			# Update the word counts
			for word in words:
				word = word.lower().strip(".,!?\"'()[]{}<>;:-")
				if word:
					total_words += 1
					if word in word_counts:
						word_counts[word] += 1
					else:
						word_counts[word] = 1
	
	# Sort the word counts by frequency in descending order
	sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
	
	# Calculate cumulative percentages
	cumulative_percentage = 0
	word_frequencies = []
	for word, count in sorted_word_counts:
		percentage = (count / total_words) * 100
		cumulative_percentage += percentage
		word_frequencies.append((word, count, percentage, cumulative_percentage))
	
	return word_frequencies, total_words

# Example usage
file_path = 'dongeng-sato-kewan/test.txt'  # Replace with the path to your .txt file
word_frequencies, total_words = count_words(file_path)

print(f"Total word count: {total_words}")
print("Word counts and cumulative percentages (sorted):")
print(f"{'Word':<15} {'Count':<10} {'Percentage (%)':<15} {'Cumulative (%)':<15}")
for word, count, percentage, cumulative_percentage in word_frequencies:
	print(f"{word:<15} {count:<10} {percentage:<15.2f} {cumulative_percentage:<15.2f}")


#'dongeng-sato-kewan/uler_sing_mertobat.txt'