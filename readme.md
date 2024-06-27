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

Wen Jie Kenneth Chen

Function 1: _parse 

Location scrapy/spiders/feed.py:150

Link to commit : 

https://github.com/tahe-ahmed/scrapy/commit/6fec39e2401ef644e3cd5f5be85969bce04d0e4c

Before instrumenting my own coverage tool code (see below):

![AD_4nXeswX9-ishZUODSt_MzUmY0dlbMzgQI4Jmk0uABnbjgJT7uCEGKBYxkpkvXSnrhrfKiVPewoyOFskngEEQrNsABkiy7CEVdv7jjIrDOjDQd8i5prKvru5_7](https://github.com/tahe-ahmed/scrapy/assets/122382588/4ad1f00c-6065-4b3c-ad61-9e5e196662e9)

After instrumenting my own coverage tool code (see below):

![AD_4nXce3JO4_rBOwZLaXxuZ3n2NXBpAratlDlPd_SX2ThMIGTElYvpc7oycBEEs9dTjPk7swuWa0vjSAmlxRYhaZObCmsZBFAqNE5uMi8HL055nI5YR3-y56ajP](https://github.com/tahe-ahmed/scrapy/assets/122382588/c5ae2948-cf7e-44e5-b4d8-1b4d3508e1e2)


The coverage tool is implemented in the same file as the function “_parse”

No branch coverage results. Because this function is not tested and covered in the existing tool. So basically it is 0%.

Wen Jie Kenneth Chen

Function 2: from_settings

Location: scrapy/spidermiddlewares/urllength.py:29

Link to commit : 

https://github.com/tahe-ahmed/scrapy/commit/7d9dd8c7874da4738ab1feb7ccd2f1615669eeea

Before instrumenting my own coverage tool code (see below):

![AD_4nXeJ5H91K5mxpQvaP8udirr3k_vw3svpv31FFRqbCwMQ80fRDxkCmrxpCO_YCUnqSDIwCwdQriVVknRmSTZkraWrXw5jHaEXdg9niMHiyhtQ4mCFcvWMESyi](https://github.com/tahe-ahmed/scrapy/assets/122382588/2cdb9572-2558-4cd8-8620-de2eb56ed041)


After instrumenting my own coverage tool code (see below):

![write_from_settings_branch_coverage_to_file()](https://github.com/tahe-ahmed/scrapy/assets/122382588/5e3d6c3d-4675-4f94-9bb7-f7f47813bd4b)

![AD_4nXeuA--tc80xifCCAWaWjoDhy66gsnz9k6UJ_pVNdedCiU6m6IU1kaasY6lq8AsWklHXEwLes_BpB-dvoB0rv9993VZFmAq35q9YWLTuC0ohe3Ro6gk4E2AK](https://github.com/tahe-ahmed/scrapy/assets/122382588/bff379b2-65a8-477b-bf7c-ad00e1ec7f9d)

Screenshot for the coverage with existing test case:

![AD_4nXf-NuExREQ6MwWOlzjIQQFf8Zqa_rmL0lzBOfpYgmELdQfYQldjh12QBJysfOWZu7ak1qiXq8NS71AHx4XBEa2Z4vwqUpC2POpy2BXEMeSuDXdFmGBsHJ2X](https://github.com/tahe-ahmed/scrapy/assets/122382588/fa7cd0e1-6c6a-47d5-b10a-44e295802165)


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

with own tool:

![AD_4nXdqk-VIuCXNlGo2RG_nG20hto9TkyJ22RZd0L7AHt5Gqnd8SPmw2-QowLTOuKLeX1J_-1a2pJ7e6i_O8hNp2hW1kVMrujJKup80_A8v-zYVnH0skMcFzBl3](https://github.com/tahe-ahmed/scrapy/assets/122382588/392cc504-ab8b-44fd-b49d-5672d2996f17)

with existing tool:

![Screenshot 2024-06-27 at 22 26 49](https://github.com/tahe-ahmed/scrapy/assets/122382588/044ba0eb-87aa-4b03-8881-b02010d8167e)

coverage went from 0% to 100% so an increase of 100 percent 

Test 2 consist of multiple tests named: 

test_get_base_setting

test_get_not_base_setting
 
test_get_bool_setting

test_get_int_setting

test_get_float_setting

test_get_list_setting

Test_default_setting

There are multiple tests since the function has 7 branches, and putting them all in 1 test function seems like bad practice.

Link to commit of the tests:

https://github.com/scrapy/scrapy/commit/24683ef8e28e625d911fc5e50bde232a8c0bde24

Screenshot of old coverage results:

with own tool:

![run_1 has been executed](https://github.com/tahe-ahmed/scrapy/assets/122382588/44aa7026-49d5-43c0-96e3-36d9b3a8789f)

with existing tool:

![Screenshot 2024-06-27 at 22 31 49](https://github.com/tahe-ahmed/scrapy/assets/122382588/91479eb8-aee1-49aa-87a6-ecb96eae8d8e)

Screenshot of new coverage results:

with own tool:

![= branch_coverage_run txt](https://github.com/tahe-ahmed/scrapy/assets/122382588/ebb0b782-f768-4629-a1e7-ca00a5a288a2)

with existing tool:

![Screenshot 2024-06-27 at 22 30 55](https://github.com/tahe-ahmed/scrapy/assets/122382588/97bbba24-2293-4038-95ba-001eff1fcc1c)

coverage went from 25% to 100% so a 75% increase in coverage
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

screenshots of old coverage result:

Screenshot of total coverage results in the coverage.xml file, to include screenshots of the whole  xml file would make it too large, but along the coverage report we used this to see branch coverage per function

![Screenshot 2024-06-27 at 22 06 48](https://github.com/tahe-ahmed/scrapy/assets/122382588/ed56d501-f394-448d-bad9-8deeac21649d

screenshots of coverage report:

![Screenshot 2024-06-27 at 22 09 15](https://github.com/tahe-ahmed/scrapy/assets/122382588/26aad9d2-70c6-4346-ae6d-f6a1a9ac8206)
![Screenshot 2024-06-27 at 22 09 28](https://github.com/tahe-ahmed/scrapy/assets/122382588/e0eb70b1-7593-43b6-a750-a5acf8f80e2c)
![Screenshot 2024-06-27 at 22 09 50](https://github.com/tahe-ahmed/scrapy/assets/122382588/5a72f671-a2d7-4f59-ab13-2c26b178b426)
![Screenshot 2024-06-27 at 22 10 04](https://github.com/tahe-ahmed/scrapy/assets/122382588/2d9a2f30-3c1e-418c-a2c6-0746c34eec3a)

screenshot of new coverage result: 

![Screenshot 2024-06-27 at 22 37 37](https://github.com/tahe-ahmed/scrapy/assets/122382588/c5f784c0-1573-48d4-b19a-32aa46096c8f)

screenshots of new coverage report:

![Screenshot 2024-06-27 at 22 38 20](https://github.com/tahe-ahmed/scrapy/assets/122382588/3791f524-f705-4330-a4f5-fd2aea187d62)
![Screenshot 2024-06-27 at 22 38 30](https://github.com/tahe-ahmed/scrapy/assets/122382588/65d016fc-1849-4965-b3af-f8b1a0cd1a63)
![Screenshot 2024-06-27 at 22 38 40](https://github.com/tahe-ahmed/scrapy/assets/122382588/aaa9cc3f-dea0-45b8-a866-d21898938e52)
![Screenshot 2024-06-27 at 22 38 47](https://github.com/tahe-ahmed/scrapy/assets/122382588/cddb1ce1-d4d7-4144-8622-e30eb325787f)


<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions
![Screenshot 2024-06-27 at 22 39 43](https://github.com/tahe-ahmed/scrapy/assets/122382588/bed45529-81f8-457d-89e4-26b023de221d)

