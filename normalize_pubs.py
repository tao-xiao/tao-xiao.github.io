import os
import re
import yaml

pub_dir = '_publications'
for filename in os.listdir(pub_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(pub_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Split frontmatter and body
        parts = re.split(r'^---', content, maxsplit=2, flags=re.MULTILINE)
        if len(parts) < 3: continue
        
        try:
            data = yaml.safe_load(parts[1])
        except Exception as e:
            print(f"Error parsing {filename}: {e}")
            continue
            
        # 1. Author Name Normalization & Attribute Removal
        if 'authors' in data:
            new_authors = []
            for author in data['authors']:
                name = author['name'] if isinstance(author, dict) else author
                # Remove <<, >>, **
                clean_name = name.replace('<<', '').replace('>>', '').replace('**', '').strip()
                new_authors.append(clean_name)
            data['authors'] = new_authors
            
        # 2. Date to Year
        if 'date' in data:
            date_str = str(data['date'])
            year = date_str.split('-')[0]
            data['year'] = int(year)
            del data['date']
            
        # 3. Abstract to Single Line
        if 'abstract' in data:
            data['abstract'] = data['abstract'].replace('\n', ' ').replace('\r', ' ').strip()
            data['abstract'] = re.sub(r'\s+', ' ', data['abstract'])
            
        # 4. Consistency: ensure is_full_paper, is_first_author, is_corresponding_author
        if 'is_full_paper' not in data:
            data['is_full_paper'] = True # Defaulting to true, user can adjust
        if 'is_first_author' not in data:
            data['is_first_author'] = False
        if 'is_corresponding_author' not in data:
            data['is_corresponding_author'] = False
            
        # Re-serialize YAML
        new_frontmatter = yaml.dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False)
        new_content = f"---\n{new_frontmatter}---" + parts[2]
        
        with open(filepath, 'w') as f:
            f.write(new_content)
