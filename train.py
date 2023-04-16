import os

parent_folder = os.path.dirname(__file__)
print(parent_folder)
data_dir = os.path.join(parent_folder, "train_data_arff")
output_dir = os.path.join(parent_folder, "outputs")
for file in os.listdir(data_dir):
    print(f"Processing file: {file}")
    file_name = file.split(".")[0]
    input_path = os.path.join(data_dir, file)
    output_path = os.path.join(output_dir, f"{file_name}.txt")
    command = f"java -classpath \"C:\Program Files\Weka-3-9-6\weka.jar\" weka.Run WekaForecaster -W \"SMOreg -C 1.0 -N 0 -I \\\"RegSMOImproved -T 0.001 -V -P 1.0E-12 -L 0.001 -W 1\\\" -K \\\"weka.classifiers.functions.supportVector.PolyKernel -E 1.0 -C 250007\\\"\" -F sales -L 1 -M 7 -G date -dayofweek -weekend -t \"{input_path}\"  -horizon 16 -prime 16 -future | findstr /r: \"....-..-..\*\"  > \"{output_path}\""
    print(f"Running command: {command}")
    os.system(command)

print("Done Hooray!!")