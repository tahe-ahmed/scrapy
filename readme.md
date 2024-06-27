# Report for Assignment 1

## Project chosen

Name: Scrapy

URL: https://github.com/scrapy/scrapy

Number of lines of code and the tool used to count it: Lizard 


Programming language: <TODO>

## Coverage measurement

### Existing tool

coverage,py 

It is executed by running the following commands: 

tox

coverage run -m tox

coverage report

Coverage xml 

overage results provided by the existing tool:

Screenshot of total coverage results in the coverage.xml file, to include screenshots of the whole  xml file would make it too large, but along the coverage report we used this to see branch coverage per function
![Screenshot 2024-06-27 at 22 06 48](https://github.com/tahe-ahmed/scrapy/assets/122382588/ed56d501-f394-448d-bad9-8deeac21649d

screenshots of coverage report:
![Screenshot 2024-06-27 at 22 09 15](https://github.com/tahe-ahmed/scrapy/assets/122382588/26aad9d2-70c6-4346-ae6d-f6a1a9ac8206)
![Screenshot 2024-06-27 at 22 09 28](https://github.com/tahe-ahmed/scrapy/assets/122382588/e0eb70b1-7593-43b6-a750-a5acf8f80e2c)
![Screenshot 2024-06-27 at 22 09 50](https://github.com/tahe-ahmed/scrapy/assets/122382588/5a72f671-a2d7-4f59-ab13-2c26b178b426)
![Screenshot 2024-06-27 at 22 10 04](https://github.com/tahe-ahmed/scrapy/assets/122382588/2d9a2f30-3c1e-418c-a2c6-0746c34eec3a)




### Your own coverage tool

<The following is supposed to be repeated for each group member>
Rutger Franken

Function 1: def _print_header  

Location: line 110 in scrapy/cmdline.py

Link to commit:

https://github.com/scrapy/scrapy/commit/bdb28b71f758b2ec3bafe6e48ea15a787e7f08c3?diff=unified&w=0

Screenshot of results outputted by the instrumentation for function1:

![Screenshot 2024-06-27 at 22 14 56](https://github.com/tahe-ahmed/scrapy/assets/122382588/70c09b3c-df1b-40c8-b365-803395ef77f7)


Function 2: def run 

Location: Line 74 in  scrapy/commands/settings.py 

Link to commit: 
https://github.com/scrapy/scrapy/commit/13799b215dcb57f0b819b5f9af0fee4fad49d5fd

Screenshot of results outputted by the instrumentation for function2:

![Screenshot 2024-06-27 at 22 16 44](https://github.com/tahe-ahmed/scrapy/assets/122382588/0c5dc5ca-be70-4fbe-9368-e2222b582a07)

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>


<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>
Rutger Franken
 
Test 1 name: test_print_header

Link to commit of test: 

https://github.com/scrapy/scrapy/commit/5de2f62d97a1078a458769813c3690201b9b5714

Screenshot of old coverage results:

with own tool:

![= branch_coverage_print_header txt x](https://github.com/tahe-ahmed/scrapy/assets/122382588/469f430e-010f-408c-ba47-c26c9d484993)

with existing tool:

![Screenshot 2024-06-27 at 22 24 17](https://github.com/tahe-ahmed/scrapy/assets/122382588/dceb2d5e-c10c-4929-a4fb-ccaf81be3c92)

Screenshot of new coverage results:

![AD_4nXdqk-VIuCXNlGo2RG_nG20hto9TkyJ22RZd0L7AHt5Gqnd8SPmw2-QowLTOuKLeX1J_-1a2pJ7e6i_O8hNp2hW1kVMrujJKup80_A8v-zYVnH0skMcFzBl3](https://github.com/tahe-ahmed/scrapy/assets/122382588/392cc504-ab8b-44fd-b49d-5672d2996f17)


<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
