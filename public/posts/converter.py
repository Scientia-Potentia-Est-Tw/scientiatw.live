import os
import frontmatter

def update_markdown_files():
    # Get all markdown files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.md')]
    
    if not files:
        print("No Markdown files found.")
        return

    for file_name in files:
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                continue

            # Identify the format by the first line
            lines = content.splitlines()
            first_line = lines[0].strip() if lines else ""
            
            if first_line == "---":
                handler = frontmatter.YAMLHandler()
                format_type = "YAML"
            elif first_line == "+++":
                handler = frontmatter.TOMLHandler()
                format_type = "TOML"
            else:
                print(f"Skipping {file_name}: No standard frontmatter detected.")
                continue

            # Parse the file with the specific handler
            post = frontmatter.loads(content, handler=handler)
            updated = False

            # logic: description -> summary
            if 'description' in post.metadata:
                post.metadata['summary'] = post.metadata.pop('description')
                updated = True

            # logic: image -> featureimage
            if 'image' in post.metadata:
                post.metadata['featureimage'] = post.metadata.pop('image')
                updated = True

            # Save back only if changes were made
            if updated:
                with open(file_name, 'w', encoding='utf-8') as f:
                    # dumps() ensures the original +++ or --- delimiters are used
                    f.write(frontmatter.dumps(post, handler=handler))
                print(f"✅ Updated {format_type}: {file_name}")
            else:
                print(f"ℹ️ No changes needed: {file_name}")

        except Exception as e:
            print(f"❌ Error processing {file_name}: {e}")

if __name__ == "__main__":
    # Requirement: pip install python-frontmatter
    update_markdown_files()