import os

# Define the base directory where your folders are located
base_dir = './samples'

# Define the folder order
folder_order = [
    'Ground_truth', 'CMT', 'Diff-BGM', 'Video2Music', 'M2UGen',
    'M2UGen_DVMSet', 'VidMuse', 'VidMuse_DVMSet', 'Ours'
]

# List of video filenames in the order you provided
video_filenames = [
    '612a0007bb9557c36f1053574df1a193.mp4',
    'e4c9fb1e93bd64ca2f987e0d33a5fb62.mp4',
    'f71d92f392d03ca1143475a5724339bd.mp4',
    'b276f3d45f38b5eeb20d091f12215fa4.mp4',
    '7e6435edc64da5af54f808446bb36bef.mp4',
    'c37bd37d8579fcb2d726aafb517349b7.mp4',
    '8e57761507eea5936bea66952393fdfa.mp4',
    'c418a0b964ad784efc9acc657f257c79.mp4',
    '16629bdad6753d4e917af0b6b87bedb4.mp4',
    '385dba274af8030b1323bc08de6ddd04.mp4',
    '2156ab88a5fa46bf5edc044e70cf3b47.mp4',
    '818437a9c748f7df125b40c10f603bf5.mp4',
    '9242b274d255672d1ffa8bd7beb795a5.mp4',
    '22ee02909930f03067220e27605636d8.mp4',
    '31a7278e9420cd59c13451e5fbf616f9.mp4',
    'd7a9505d9761a69a02c4203dbd72fb5a.mp4',
    '95caf2d2919397a7c3ac441c8a9902a9.mp4',
    '9c5d8002a0c2a7e20ff38b06491b9bfd.mp4'
]

# Start the HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VidMusician Demo</title>
    <style>
        .video-group {
            margin-bottom: 40px;
        }
        .video-row {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .video-container {
            width: 18%;
            margin-bottom: 20px;
        }
        .video-container video {
            width: 100%;
            height: auto;
        }
        .folder-name {
            text-align: center;
            font-size: 1em;
            margin-bottom: 5px;
        }
        .empty-slot {
            width: 18%;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.5em;
            margin-top: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        .note {
            font-size: 1.2em;
            color: gray;
            text-align: center;
            margin-bottom: 20px;
        }
        .nav-buttons {
            text-align: left;
            width: 40%;
            margin-bottom: 20px;
            margin-left: 20px;
        }
        .nav-buttons a {
            display: block;
            margin: 10px 0;
            text-decoration: none;
            font-size: 1.2em;
            color: #000;
            padding: 10px;
            background-color: #F1F9F4;
            border-radius: 5px;
        }
        .nav-buttons a:hover {
            background-color: #F1F9F4;
        }
        .intro {
            text-align: left;
            margin: 20px;
            font-size: 1.2em;
        }
        .group-buttons {
            display: flex;
            flex-wrap: wrap;
            justify-content: left;
            margin-bottom: 20px;
            margin-left:20px;
        }
        .group-buttons a {
            margin: 5px;
            padding: 10px 15px;
            text-decoration: none;
            font-size: 1em;
            color: black;
            background-color: #F1F9F4;
            border: none;
            border-radius: 5px;
        }
        .group-buttons a:hover {
            background-color: #F1F9F4;
        }
        .main-title {
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .sub-title {
            text-align: center;
            font-size: 1.2em;
            color: gray;
        }
    </style>
</head>
<body>
<div class="main-title">VidMusician: Video-to-Music Generation with Semantic-Rhythmic Alignment via Hierarchical Visual Features</div>
<div class="sub-title">Paper ID 4035</div>
<div class="intro">
    <p>This page is divided into two sections: Comparison with Other Methods and Results of Our Method on AI-Generated Videos.</p>

</div>
<p style="margin-left: 20px;">For the first section, you can click the buttons below to jump to different groups. DVMSet suffix represents training the model with our Dataset. </p>
<div class="group-buttons">

'''
# Add buttons for each group
for idx in range(1, 19):
    html_content += f'<a href="#group_{idx}">Group {idx}</a>\n'

html_content += '''
</div>
<p style="margin-left: 20px;">For the second section, you can click the button below to jump to it.</p>
<div class="nav-buttons">
    <a href="#ai-results">Results of Our Method on AI-Generated Videos</a>
</div>


'''

# First section: Compare with Other Methods
html_content += '<div id="compare" class="section-title">1. Comparison with Other Methods</div>\n'
# html_content += '<p class="note">DVMSet suffix represents training the model with our Dataset.</p>\n'

# Loop through each video filename and add videos from each folder to the HTML content
for idx, video_filename in enumerate(video_filenames):
    html_content += f'<div id="group_{idx + 1}" class="video-group">\n'
    html_content += f'    <div class="video-row">\n'
    html_content += f'        <div class="folder-name">Group_{idx + 1}</div>\n'
    html_content += f'    </div>\n'
    html_content += f'    <div class="video-row">\n'
    for i, folder in enumerate(folder_order[:5]):
        video_path = os.path.join(base_dir, folder, video_filename)
        html_content += f'        <div class="video-container">\n'
        html_content += f'            <div class="folder-name">{folder}</div>\n'
        html_content += f'            <video controls>\n'
        html_content += f'                <source src="{video_path}" type="video/mp4">\n'
        html_content += f'                Your browser does not support the video tag.\n'
        html_content += f'            </video>\n'
        html_content += f'        </div>\n'
    html_content += f'    </div>\n'
    html_content += f'    <div class="video-row">\n'
    for i, folder in enumerate(folder_order[5:]):
        video_path = os.path.join(base_dir, folder, video_filename)
        html_content += f'        <div class="video-container">\n'
        html_content += f'            <div class="folder-name">{folder}</div>\n'
        html_content += f'            <video controls>\n'
        html_content += f'                <source src="{video_path}" type="video/mp4">\n'
        html_content += f'                Your browser does not support the video tag.\n'
        html_content += f'            </video>\n'
        html_content += f'        </div>\n'
    # Add an empty slot to align with the first row
    html_content += f'        <div class="empty-slot"></div>\n'
    html_content += f'    </div>\n'
    html_content += f'</div>\n'

# Second section: Our Results of AI-generated videos
html_content += '<div id="ai-results" class="section-title">2. Results of Our Method on AI-Generated Videos</div>\n'

# Get the list of video filenames in the AI folder
ai_video_filenames = [f for f in os.listdir(os.path.join(base_dir, 'AI')) if f.endswith('.mp4')]

# Loop through each video filename in the AI folder and add videos to the HTML content
html_content += f'<div class="video-group">\n'
html_content += f'    <div class="video-row">\n'
for idx, video_filename in enumerate(ai_video_filenames):
    video_path = os.path.join(base_dir, 'AI', video_filename)
    html_content += f'                <div class="video-container">\n'
    html_content += f'            <video controls>\n'
    html_content += f'                <source src="{video_path}" type="video/mp4">\n'
    html_content += f'                Your browser does not support the video tag.\n'
    html_content += f'            </video>\n'
    html_content += f'        </div>\n'
    if (idx + 1) % 4 == 0:
        html_content += f'    </div>\n'
        html_content += f'    <div class="video-row">\n'
# If the last row is not full, add empty slots
if len(ai_video_filenames) % 4 != 0:
    for _ in range(4 - (len(ai_video_filenames) % 4)):
        html_content += f'        <div class="empty-slot"></div>\n'
html_content += f'    </div>\n'
html_content += f'</div>\n'

# Close the HTML content
html_content += '''
</body>
</html>
'''

# Write the HTML content to a file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file generated successfully.")