context({
  testcase("d20 werd correct berekenend.", {
    testEqual(NULL, function(student_env) {
      mean(student_env$d20)
    }, 10.441)
  })
  testcase("De volgende functie werd gebruikt:", {
    testFunctionUsed("mean")
  })
}, preExec = {
  set.seed(1234)
})