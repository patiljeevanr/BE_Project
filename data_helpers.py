# hearers
import glob

# data loading functions
def load_data(list_of_files):
    return [line.rstrip() for filename in list_of_files for line in open(filename, encoding = 'UTF-8', errors='ignore')]

# accessing files marathi
marathi_files = glob.glob('/home/pravin/29-2-16/data_new/Marathi/*.txt')
data_marathi = load_data(marathi_files)

# accessing files hindi
hindi_files = glob.glob('/home/pravin/29-2-16/data_new/Hindi/*.txt')
data_hindi = load_data(hindi_files)

# whole data
X_train = data_marathi + data_hindi

# marathi labels
marathi_labels = ['Marathi' for _ in data_marathi]

# hindi labels
hindi_labels = ['Hindi' for _ in data_hindi]

# whole labels
y_train = marathi_labels + hindi_labels

# save data train
outfile_X_train = open('/home/pravin/29-2-16/data_new/train_data', 'w', encoding = 'utf-8')
outfile_X_train.write("\n".join(X_train))

# save data labels
outfile_y_train = open('/home/pravin/29-2-16/data_new/train_labels', 'w', encoding = 'utf-8')
outfile_y_train.write("\n".join(y_train))

print("data loaded...")
