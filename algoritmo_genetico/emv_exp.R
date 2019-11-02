# vero_exp = function(lambda, amostra){
#   n = length(amostra)
#   resultado = lambda^n * exp(-lambda * sum(amostra))
#   if(resultado == "NaN") resultado = 0
#   return(resultado)
# }

vero_exp = function(lambda, amostra){
  n = length(amostra)
  val = n*log(lambda) - lambda*sum(amostra)
  if(val == 'NaN') val = 0
  return(val)
}

fitness = function(pop,amostra){
  f = mapply(function(x) vero_exp(x,amostra),pop)
  data = data.frame("function" = f,
                    "lambda" = pop)
  data = dplyr::arrange(data,function.)
  data = dplyr::mutate(data,ind = 1:length(pop) )
  data = dplyr::select(data, ind, dplyr::everything())
  data = dplyr::mutate(data, prob = ind/sum(ind))
  return(data)
}

escolhe = function(data){
  pais = sample(data$lambda,2,prob = data$prob)
  return(pais)
}

crossover = function(pais,n){
  filhos = c()
  for( i in 1:n){
    prob = runif(1,0,1)
    filhos = c(filhos,prob*pais[1] + (1-prob)*pais[2])
  }
  return(filhos)
}

mutacao = function(filhos){
  for(i in 1:length(filhos)){
    prob = runif(1,0,1)
    if(prob > 0) filhos[i]=filhos[i]+runif(1,-5,5)
  }
  return(filhos)
}

inicia = function(n){
  pop = runif(n,0,10)
  return(pop)
}

amostra = rexp(300,18)
pop = inicia(10)
for(i in 1:1000){
  data = fitness(pop,amostra)
  pais = escolhe(data)
  filhos = crossover(pais,10)
  filhos = mutacao(filhos)
  pop = filhos
  data = fitness(pop,amostra)
}
estimativa =data$lambda[which.max(data$function.)]
estimativa
