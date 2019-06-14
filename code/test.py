import model.config as config
filepath = config.base_folder + "data/basic_data/wiki_name_id_map.txt"
# filepath= "D:\\Cinnamon\\Knowledge_graph\\end2end_neural_el\\wiki_name_id_map.txt"
import json
name=[]
id=[]
with open(filepath, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line_splited=line.strip().split()
        name.append(' '.join(line_splited[:len(line_splited)-1]))
        id.append(int(line_splited[-1]))
    f.close()
print("number: ", len(id))
print('max_id: ', max(id))
max_id= max(id)
def write_new_data(json_file):
    new_idx_file= open( config.base_folder + "data/basic_data/new_wiki_name_id_map.txt", 'w')
    with open(json_file, 'r', encoding='utf-8') as f:
        data= json.load(f)
        f.close()
    

