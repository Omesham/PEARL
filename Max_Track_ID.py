def determine_max_track_id(self):
        all_track_ids = set()
        
        for sequence_folder in self.sequence_folders:
            sequence_path = os.path.join(self.dataset_path, sequence_folder)
            label_folder = os.path.join(sequence_path, 'labels')
            if not os.path.exists(label_folder):
                continue

            for label_file in sorted(os.listdir(label_folder)):
                if not label_file.endswith('.txt'):
                    continue

                with open(os.path.join(label_folder, label_file), 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line_split = line.strip().split(' ')
                        if len(line_split) < 6:
                            continue

                        track_id = int(line_split[5])
                        all_track_ids.add(track_id)

        return max(all_track_ids)  
    
    
    
