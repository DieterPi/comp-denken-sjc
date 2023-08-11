context({
  testcase("Het gemiddelde van de vector werd correct berekend.", {
    testEqual(NULL, function(student_env) {
      mean(student_env$N_estimated)
    }, 1024.4)
  })
  testcase("De \"as.integer\" functie werd gebruikt.", {
    testFunctionUsedInVar("as.integer", "N_estimated")
  })
}, preExec = {
  set.seed(1234)
})