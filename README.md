# SensAi

This is the code for a Facebook messenger bot that allows the user to find the URL to an ASL video representation based on an input word. The messenger bot uses Wit.AI and NLP to guess with confidence % what the word in a user question is and finds the word's link in the database. Project was done as part of the AI for Social Good Hackathon hosted by McGill University.

Work is done using: Node.js, Python, CSV, Wit.AI, Messenger Facebook Developer Tools, Webhook and ngrok.


1) Creating Our Own Dataset</h3>
As there weren't any clean existing dataset of ASL translated videos of common English word, the handspeak website did have a fair amount of 7553 videos for common words. We thought it would be a great start to find links to these videos and being able to map them to the word associated. We used Python to scrape the website and create a dataset. Although the links for the video's .mp4 location couldn't be easily shared because of permission issues, the dataset still allowed us to map the numbers to the correct word and its webpage. The Python program for this is called <a href="https://github.com/archidisign/SensAi/blob/master/DBExtract.py">DBExtract.py</a>. The program scrapes the website's structure and saves all important information in a csv file.
<ul>
 	<li>Link: Handspeak <a href="https://medium.com/@Oskarr3/developing-messenger-bot-with-ngrok-5d23208ed7c8">website</a></li>
</ul>
<h3>2) Using Wit.AI</h3>
We then created an account on Wit.AI, an online application owned by Facebook. This application allows the user to create a chatbot, train it on sample expressions to recognize what the user is saying and allowing to return an output by the bot. Furthermore, it also allows to do back-end work using Node.js, Python and other languages. We used it to first train our model to recognize expressions like "How do you say WORD?" and "What is WORD in ASL?". The back-end to keep track of these expressions and return the output based on the confidence perentage was done using the node-wit repositary on github, available <a href="https://github.com/wit-ai/node-wit">here</a>. Make sure to have Node.js installed before you use the code.

<a href="https://catharticstudent.files.wordpress.com/2017/07/wit.jpg"><img class="alignnone size-full wp-image-745" src="https://catharticstudent.files.wordpress.com/2017/07/wit.jpg" alt="" width="820" height="286" /></a>
<ul>
 	<li>Link: Wit.AI <a href="https://wit.ai/docs/quickstart">quickstart </a>tutorial</li>
</ul>
<h3>3) Creating a Facebook Page to Host the Messenger Bot using Ngork</h3>
The next step was to go on Facebook to create a new facebook page. We found this nice tutorial that explains step by step how to create a chatbot on facebook and how to connect it to our code. However, instead of using Heroku to host the chatbot, we simply wanted it to run locally on our own laptop. Hence, we decided to use Ngork instead. Here is another extremely handy tutorial that explains how to run the code using it. Make sure you have a hidden file .env where all your tokens are initialized with the proper value.
<ul>
 	<li>Links: <a href="https://blog.hartleybrody.com/fb-messenger-bot/">Tutorial 1</a>, <a href="https://medium.com/@Oskarr3/developing-messenger-bot-with-ngrok-5d23208ed7c8">Tutorial 2</a></li>
</ul>
<h3>4) Test and Results</h3>
<p style="text-align: left;">To test the chatbot, run on your command-line both the messenger.js file using Node and open a local port using ngrok.</p>
<p style="text-align: center;"><code> ./ngrok http 8445 </code>
<code> node messenger.js </code></p>
You are now connected and can see immediate result. Here, I tested the chatbot and was pleasantly surprised to see that everything is working as expected. If you look at the command-line, you will also be able to track the confidence percentage for each expression being entered.

<a href="https://catharticstudent.files.wordpress.com/2017/07/fb_dev3.jpg"><img class="alignnone size-full wp-image-746" src="https://catharticstudent.files.wordpress.com/2017/07/fb_dev3.jpg" alt="" width="802" height="244" /></a> <a href="https://catharticstudent.files.wordpress.com/2017/07/fb_dev.jpg"><img class="alignnone size-full wp-image-747" src="https://catharticstudent.files.wordpress.com/2017/07/fb_dev.jpg" alt="" width="820" height="206" /></a> <a href="https://catharticstudent.files.wordpress.com/2017/07/fb_dev2.jpg"><img class="alignnone size-full wp-image-748" src="https://catharticstudent.files.wordpress.com/2017/07/fb_dev2.jpg" alt="" width="820" height="107" /></a> <a href="https://catharticstudent.files.wordpress.com/2017/07/ngork.jpg"><img class="alignnone size-full wp-image-749" src="https://catharticstudent.files.wordpress.com/2017/07/ngork.jpg" alt="" width="820" height="427" /></a>
A video demo at <a href="https://github.com/archidisign/SensAi/blob/master/sensAI_test.mp4">here</a>
