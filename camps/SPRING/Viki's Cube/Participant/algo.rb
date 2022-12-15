require_relative "rubic.rb"

############ Arrete blanche ############

def arrete_blanche_formule_cote(ru)
  #####
  #code à inséré ici#
  ###
end


def arrete_blanche_formule_face(ru)
  #####
  #code à inséré ici#
  ###
end



def arrete_blanche(ru)
  r = ru.check

  for i in 1..4
    if r[0][0][1] == r[0][1][1] and r[1][0][1] == r[1][1][1] and r[2][0][1] == r[2][1][1] and r[3][0][1] == r[3][1][1]
      break
    end
    ru.u
  end

  for j in 1..4
    for i in 1..2
      if r[1][0][1] == r[1][1][1] and r[3][0][1] == r[3][1][1]
        #########
        arrete_blanche_formule_face ru
      end
      ru.u
    end
    for i in 1..4
      if r[2][0][1] == r[2][1][1] and r[3][0][1] == r[3][1][1]
        arrete_blanche_formule_cote ru
        return
      end
      ru.u
    end
    ru.transform_left
  end
end

########### Coins Blancs ###############

def is_cible_correct?(r)
  r[4][2][2] == r[4][1][1] and r[1][0][2] == r[1][1][1] and r[2][0][0] == r[2][1][1]
end

def get_coin_cible(r)
  [r[4][1][1], r[1][1][1], r[2][1][1]]
end

def get_coin_haut(r)
  [r[4][2][2], r[1][0][2], r[2][0][0]]
end

def get_coin_bas(r)
  [r[1][2][2], r[5][0][2], r[2][2][0]]
end

def coins_blanc_formule(ru)
  ############
  ru.rp
  ru.dp
  ru.r
  ru.d
end

def coins_blanc(ru)
  r = ru.check

  for i in 0..3
    if (get_coin_haut(r).include?(r[4][1][1]))
      while get_coin_bas(r).include?(r[4][1][1])
        ru.d
      end
      coins_blanc_formule ru
    end
    ru.transform_right
  end

  for i in 0..3
    until is_cible_correct? r
      if (get_coin_cible(r) & get_coin_bas(r)).length == 3 or (get_coin_cible(r) & get_coin_haut(r)).length == 3
        until is_cible_correct? r
          coins_blanc_formule ru
        end
      end
      ru.d
    end
    ru.transform_right
  end
end

########### 2e Couronne ###########

def is_2couronne_correct?(r)
  for i in 0..3
    unless (r[i][1][0] == r[i][1][1]) and (r[i][1][1] == r[i][1][2])
      return false
    end
  end
  return true
end

def deuxieme_couronne(ru)
  r = ru.check

  until is_2couronne_correct? r
    for i in 0..3
      if (r[1][0][1] == r[1][1][1] and r[4][2][1] == r[0][1][1]) or (r[1][1][0] == r[0][1][1] and r[1][1][0] == r[1][1][1])
        #####
        #code à inséré ici#
        ###
      elsif (r[1][0][1] == r[1][1][1] and r[4][2][1] == r[2][1][1]) or (r[1][1][2] == r[2][1][1] and r[2][1][0] == r[1][1][1])
        #####
        #code à inséré ici#
        ###
      end
      ru.up
    end
    ru.transform_right
    r = ru.check
  end
end

########### croix jaune ###########

def croix_jaune_seq(ru)
  ##############
  #####
  #code à inséré ici#
  ###
end

def croix_jaune(ru)
  r = ru.check

  if r[4][0][1] == r[4][1][1] and r[4][1][0] == r[4][1][1] and r[4][2][1] == r[4][1][1] and r[4][1][2] == r[4][1][1]
    return
  end

  for i in 0..4
    if r[4][0][1] == r[4][1][1] and r[4][1][0] == r[4][1][1]
      croix_jaune_seq ru
      break
    elsif r[4][0][1] == r[4][1][1] and r[4][1][1] == r[4][2][1]
      croix_jaune_seq ru
      croix_jaune_seq ru
      break
    end
    ru.u
  end
  
  unless r[4][0][1] == r[4][1][1] and r[4][1][0] == r[4][1][1] and r[4][2][1] == r[4][1][1] and r[4][1][2] == r[4][1][1]
    croix_jaune_seq ru
    ru.u
    croix_jaune_seq ru
  end
end

######## Placement coins ##########

def placement_formule(ru)
  #########
  #####
  #code à inséré ici#
  ###
end

def coin_bien_place(r)
  ([r[1][0][2], r[4][2][2], r[2][0][0]] & [r[1][1][1], r[4][1][1], r[2][1][1]]).length == 3
end

def placement_coins(ru)
  r = ru.check

  #####
  #code à inséré ici#
  ###

  if coin_bien_place(r)
    #####
    #code à inséré ici#
    ###

    unless coin_bien_place(r)
      #####
      #code à inséré ici#
      ###
    end
    ru.transform_left
  else
    #####
    #code à inséré ici#
    ###
  end
end

######## Coins Jaune #########

def is_jaune_correct?(r)
  r[4][2][2] == r[4][1][1]
end

def coins_jaune(ru)
  r = ru.check

  until
    #####
    #code à inséré ici#
    ###
  end

  for i in 0..3
    #####
    #code à inséré ici#
    ###
  end
end

#############################

def algo(ru)
  ru.transform_up # On tourne tout le rubik vers le haut 

  print ru

  arrete_blanche ru
  print " ----  Arrete ----\n", ru

  coins_blanc ru
  print " ----  Face Blanche ----\n", ru

  # On retourn horizontalement le rubik 
  ru.transform_down 
  ru.transform_down

  deuxieme_couronne ru
  print " ----  2e Couronne ----\n", ru
  
  croix_jaune ru
  print " ----  Croix Jaune ----\n", ru
  
  arrete_blanche ru
  print " ----  Arrete Jaunes ----\n", ru
  
  placement_coins ru
  print " ----  Placements coins Jaunes ----\n", ru
  
  coins_jaune ru
  print " ----  Fin ----\n", ru
end

ru = Rubic.new(filename)
# ru.numberize false
ru.colorize true

algo ru