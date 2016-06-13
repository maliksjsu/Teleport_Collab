// Create a custom Cloud9 runner - similar to the Sublime build system
// For more information see https://docs.c9.io/custom_runners.html

{
    "cmd": [
        "bash",
        "--login",
        "-c",
        "cd /home/ubuntu/workspace/flask_init/chef_browser && source venv2.7/bin/activate && python manage.py runserver"
    ],
    "working_dir": "$project_path",
    "info": "Your code is running at \\033[01;34m$url\\033[00m.\n\\033[01;31m"
}