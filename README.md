# AutoML-Extensions-Screening-Exercise

## Answer: 114

With updated value for random seed (i.e. 11), the first change of champion occurs at example **114**.

Used python script to programatically update champion change value in the code. The idea is simply to iterate over all possible values and re-build for the unit-test and run tests until no error is encountered.

The python script can be accessed from script.py.

### Implementation Details

- Iterate from 0 to 1331. Build and run unit test for each possibility until the tests pass. This is automated using python script.
- The value for which test passes without any error is essentially the example at which champion change occurs for the new seed value.

### Reproduce the approach

- Manually update the value of random seed in the file `vowpal_wabbit/test/unit_test/automl_test.cc` from 10 to 11.
- Place script.py in the root directory of the project i.e. in vowpal_wabbit directory.
- Run the script.
