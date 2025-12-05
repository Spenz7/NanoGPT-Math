# Please download the pretrained NanoGPT model on QA data from the [link](https://drive.google.com/file/d/1gIZw-HAB-tHtEYCmNugwlIV7R3WsgjjZ/view?usp=sharing), and place it into the folder `./sft`!

# If you have any questions, please feel free to open an issue on GitHub, and I will respond.

Keep gpt.pt locally for each collaborator.

Each person working on the project downloads gpt.pt separately from the original source and places it in sft/.

Since it’s in .gitignore, it won’t be pushed to GitHub, so your repo stays under GitHub’s 100 MB limit.

Need GPU to train the model 10x quicker (40mins for 10 epochs)

Since my laptop has no GPU, need to use Colab's GPU istd, it's an online website

To do so, need dpo(forColabDpoTestOnly).ipynb, which is modified from dpo.ipynb as it has extra first few cells to import Github repo (cuz u need the files there) and modifies the file paths in its code to acc them. Had to use this mtd as Colab's option to import github stuff allowed me to import my github repo, but I couldn't open the dpo.ipynb file in code format.

However, now there's Colab extension in VsCode (came out after I finished this project), so maybe I won't need to do the para abv anymore. Read below for more info:
https://marketplace.visualstudio.com/items?itemName=Google.colab


