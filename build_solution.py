

pages = [
	{
	"filename": "content/middle_about.html",
	"output": "docs/about.html",
	"title": "About",
	},
	
	{
	"filename": "content/middle_portfolio.html",
	"output": "docs/portfolio.html",
	"title": "Portfolio", },
	
	{
	"filename": "content/middle_index.html",
	"output": "docs/index.html",
	"title": "Index", },
	
	{
	"filename": "content/middle_contact.html",
	"output": "docs/contact.html",
	"title": "Contact", } ]
	


	
def opentemplate():		
	#open and read the base template file
	template = open("templates/base.html").read()
	#return the template file so other functions can use it
	return template



def opencontent():
	for page in pages:
		#define filename from list of dictionaries
		filename = page["filename"]
	
		#open content file
		content = open(filename).read()
		return content
		
		
def output():
	for page in pages:
		#define output file path from list of dictionaries
		output = page["output"]
		#define title from list of dictionaries
		title = page["title"]
		#call on template function
		template = opentemplate()
		#call on content function
		content = opencontent()
		#replate content in template document
		finished_page = template.replace("{content}", content).replace("{title}", title)
		#write new finished page doc
		open(output, "w+").write(finished_page)

		
opentemplate()	
opencontent()
output()


