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

![Screenshot 2024-06-27 at 22 56 33](https://github.com/tahe-ahmed/scrapy/assets/122382588/2dd7fe82-2d8f-438d-be13-e5d5c39964c8)


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

Peter Mayrany
Function 5: print_requests():
Location: scrapy/commands/parse.py
Git commit line:
https://github.com/tahe-ahmed/scrapy/commit/3e66201b9477ef923a611cf906f7c8015f0ee307 
The above commit includes the instrumentation for both functions, since they are in the same file.

Before adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/5a41feee-75b7-4c5b-bcfa-9f5ba520caa7)

Function 6: max_level()
Location: scrapy/commands/parse.py

Before adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/b20d1c40-0d68-4bda-b50a-75bf1145aae9)



---

    
    
**Tahe Ahmed Ghaleb Alhamady**
### Function 7: `def initiate_request`

**Location:** `Stream.py`

**Link to commit:**  
[https://github.com/tahe-ahmed/scrapy/commit/020db210479b7692b32671f35a7a3a0c46416936](https://github.com/tahe-ahmed/scrapy/commit/020db210479b7692b32671f35a7a3a0c46416936)

**Screenshot of results outputted by the instrumentation for Function 1:**

![Screenshot from 2024-06-24 20-33-28](https://github.com/tahe-ahmed/scrapy/assets/61438389/513d5267-f57e-4729-aae4-3668db16b68a)

### Function 8: `def window_updated`

**Location:** `protocol.py`

**Link to commit:**  
[https://github.com/tahe-ahmed/scrapy/commit/020db210479b7692b32671f35a7a3a0c46416936](https://github.com/tahe-ahmed/scrapy/commit/020db210479b7692b32671f35a7a3a0c46416936)

**Screenshot of results outputted by the instrumentation for Function 2:**

![Screenshot from 2024-06-24 20-33-28](https://github.com/tahe-ahmed/scrapy/assets/61438389/088d1fd8-cb1d-4887-b2fe-d666a0be1c74)

    

---


---


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



Wen Jie Kenneth Chen

Test 3: Consist 2 test functions

Location: tests/test_spider.py

Namely: 

1. test_parse_without_parse_row
  
2. test_parse_with_parse_row

Link to commit:

https://github.com/tahe-ahmed/scrapy/commit/c32a1b0042c02d382c3ab9f62633a0a7de1a6fab

Screenshots of the tests:

![AD_4nXd3NOZ95j_qjbG4_lc5lslME5MzT28sp3vihkecX2z-eAo_gf4rksW-c8suHOa9ycc5B-Pc_v2LCQyPfhdt2DiLRCkV3k0iCOgL03xTI2VYK7-Bup_c9K39](https://github.com/tahe-ahmed/scrapy/assets/122382588/392d614b-940b-4579-8a0d-d3c44149e36b)

![AD_4nXcOb-Bszkwekr-XwfaCB71MnRLpOHZN214huEGdDuMcw688-D-Vppsu2yKTP99QNcfOSf6A_P50tseJXzj07yGc9IFSj8xExnMz7FQalutmGyjhOvpMZ21r](https://github.com/tahe-ahmed/scrapy/assets/122382588/81b1e696-c4e6-4f1e-ba96-452df7329b66)

No old coverage screenshot for this function.

Because the function is not covered and not tested.

So the branch coverage for that function is 0%

New coverage screenshot for this function:

![= branch_coverage_parse txt](https://github.com/tahe-ahmed/scrapy/assets/122382588/055674c2-a33e-46a8-ad1b-0ad59603241c)


Test 4: consist 3 test functions. (Actually 1 is enough but the other is not tested because it is setup. So i made 1 additional test that actually test it.

Location: tests/test_spidermiddlewares_urllength.py

Namely: 

1. setUp
3. test_from_settings_not_configured
4. test_from_settings_configured

Link to commit: 
https://github.com/tahe-ahmed/scrapy/commit/9b5a6ec8e7421eba800179b0b471add39042ed67

Screenshot of existing function that covered 50% branch of “from_settings”:

(Note: it is a setup function but it covers 50% branches and it is not tested. I added  test cases for both.)

![AD_4nXfpVEd89o8aTpGbL5yG_zk1HeypKPlgoZCsDLXtwd6--GFgDdI4YxxFCPWWWo_VGi_qNsnjLbBNK4MHT0spl8ULHJlRRsZRHSjAdOzGti084CXNtdV7_VJJ](https://github.com/tahe-ahmed/scrapy/assets/122382588/28cc9eab-fa7c-4da6-be6d-e2b48602c03e)

New test functions:

![AD_4nXciQJLBpebRIDdQKqhRx69sim_k99iPfxcQLXn6gjLC6ubu5RVahIhNoW-KqFb3_Y2jOSdFdroPMxm_EPAhQNza2ciaX1RRjmjt6YpWnuWrSWn01BWbzjW8](https://github.com/tahe-ahmed/scrapy/assets/122382588/91b3df16-dc88-4bb3-881a-0575f44dd409)

old screenshot coverage:

![brancht has been missed](https://github.com/tahe-ahmed/scrapy/assets/122382588/555c6f9c-08d3-4854-b4a1-73578d282675)

New screenshot coverage:

![= branch_coverage_from_settings txt](https://github.com/tahe-ahmed/scrapy/assets/122382588/74a96768-98c9-473d-a454-9891a16adfad)


The setup function already covered 50% because it called from_settings but it was not really tested with assert, so i made an additional test case for it.
Now with the third test function the coverage will be 100%.

---
Function 5: print_requests()
Test 5 Commit link:
https://github.com/tahe-ahmed/scrapy/commit/6bf57c71a459b9ae59f417bb1049d6ffe0a1c6e8 

Before running adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/c5f19a68-b6da-4cf8-9495-8cbc9c5c1a6f)

After running adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/de26788c-b0b9-4a9b-9ede-9b39f7de2982)

The screenshot above shows that 5 statements have been covered and a 3% increase statement coverage for parse.py

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/97e277c8-cfcf-4596-b705-ae038680e954)

The coverage was initially 0%, meaning none of the branches were covered. After adding test cases that account for all the possible paths from the decision points, the branch coverage increased to 100%. For this test the test cases used were:
test_max_Lvl_no_items_no_requests()
test_max_Lvl_with_items_no_request()
test_max_Lvl_no_items_with_request()
test_max_Lvl_with_items_with_request()

Function 6: max_level()
Test 6 Commit link: 
https://github.com/scrapy/scrapy/commit/19cf241ad0e8d1e477ec786baec2894405fda0b7  

Before adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/f0a379f5-7402-4d9d-b8f5-b5da8bdae498)

After adding the test cases:

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/cee8fdcf-33ae-4957-a85b-a2cc2cdd081b)

The screenshot above shows that 6 statement have been covered and a 3% increase statement coverage for parse.py

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/53c7894c-0a5c-448e-ba3d-988a79949fbe)

For this function, the process is similar to the aforementioned function, however, 2 else cases were created to account for the “invisible” branch and update the dictionary when the branch gets covered. The following were the test cases used:
test_print_requests_no_level_no_request
test_print_requests_no_level_with_request
test_print_requests_with_level_with_request
test_print_requests_with_level_no_request

![image](https://github.com/tahe-ahmed/scrapy/assets/66109992/3f32e418-29f6-4cf6-bc19-ca12a74c58dd)

---

     
**Tahe Ahmed Ghaleb Alhamady**
    
**Test 7 name: test_window_updated_specific_stream():		
Test 8 name: test_window_updated_all_streams():**

Location : tests/test_core_http2_protocol.py
Location: tests/test_core_http2_stream.py

Link to commit of tests: 

https://github.com/tahe-ahmed/scrapy/commit/020db210479b7692b32671f35a7a3a0c46416936

* Old coverage results: 

    * with my own coverage tool:
     ![Screenshot from 2024-06-24 20-33-28](https://github.com/tahe-ahmed/scrapy/assets/61438389/b3901838-91ac-44ed-961a-a6d6adc4aec6)

    * with the [coverage.py](https://coverage.readthedocs.io/en/7.5.4/) tool: 
![Screenshot from 2024-06-27 23-19-58](https://github.com/tahe-ahmed/scrapy/assets/61438389/ba74ed0d-d5ae-4400-896f-5b68df8d0b75)
![Screenshot from 2024-06-27 23-19-10](https://github.com/tahe-ahmed/scrapy/assets/61438389/d25e4ae4-e6c3-45dc-aea2-b221a71d55d3)

* New coverage results:
 
 
    * with my own coverage tool:
  ![Screenshot from 2024-06-24 20-43-27](https://github.com/tahe-ahmed/scrapy/assets/61438389/d17def5a-a171-4d8d-a7de-0d46c407d61d)

    * with the [coverage.py](https://coverage.readthedocs.io/en/7.5.4/)  tool:
![Screenshot from 2024-06-27 23-23-28](https://github.com/tahe-ahmed/scrapy/assets/61438389/de17da27-f31c-4500-8074-b51e62f3585a)
![Screenshot from 2024-06-27 23-23-05](https://github.com/tahe-ahmed/scrapy/assets/61438389/ea3f01ef-9237-465b-9aca-ab90f24f4132)

---
---


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

