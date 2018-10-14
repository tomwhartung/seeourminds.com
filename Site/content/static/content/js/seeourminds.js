/*
 * Code for general use on seeourminds.com
 */
var seeourminds = {};

/**
 * Set the name of the transition effect desired
 * for each four letter type, to add some variety
 * Note: the "pulsate" effect is a bit annoying.
 */
seeourminds.effect_for_type = {
  'ENFJ': 'shake',
  'ENFP': 'bounce',
  'ENTJ': 'explode',
  'ENTP': 'drop',
  'ESFJ': 'puff',
  'ESFP': 'explode',
  'ESTJ': 'shake',
  'ESTP': 'highlight',
  'INFJ': 'blind',
  'INFP': 'fold',
  'INTJ': 'scale',
  'INTP': 'fade',
  'ISFJ': 'size',
  'ISFP': 'slide',
  'ISTJ': 'highlight',
  'ISTP': 'clip',
}

/**
 * Set the name of the color corresponding to the
 * dominant function for each four letter type
 */
seeourminds.color_name_for_dom = {
  'ENFJ': 'Red',
  'ENFP': 'Blue',
  'ENTJ': 'Green',
  'ENTP': 'Blue',
  'ESFJ': 'Red',
  'ESFP': 'Yellow',
  'ESTJ': 'Green',
  'ESTP': 'Yellow',
  'INFJ': 'Blue',
  'INFP': 'Red',
  'INTJ': 'Blue',
  'INTP': 'Green',
  'ISFJ': 'Yellow',
  'ISFP': 'Red',
  'ISTJ': 'Yellow',
  'ISTP': 'Green',
}

/**
 * Set the name of the color corresponding to the
 * auxiliary function for each four letter type
 */
seeourminds.color_name_for_aux = {
  'ENFJ': 'Blue',
  'ENFP': 'Red',
  'ENTJ': 'Blue',
  'ENTP': 'Green',
  'ESFJ': 'Yellow',
  'ESFP': 'Red',
  'ESTJ': 'Yellow',
  'ESTP': 'Green',
  'INFJ': 'Red',
  'INFP': 'Blue',
  'INTJ': 'Green',
  'INTP': 'Blue',
  'ISFJ': 'Red',
  'ISFP': 'Yellow',
  'ISTJ': 'Green',
  'ISTP': 'Yellow',
}

/**
 * Set the bootstrap class for the color corresponding to the
 * dominant function for each four letter type
 */
seeourminds.bootstrap_class_for_dom = {
  'ENFJ': 'btn-red',
  'ENFP': 'btn-blue',
  'ENTJ': 'btn-green',
  'ENTP': 'btn-blue',
  'ESFJ': 'btn-red',
  'ESFP': 'btn-yellow',
  'ESTJ': 'btn-green',
  'ESTP': 'btn-yellow',
  'INFJ': 'btn-blue',
  'INFP': 'btn-red',
  'INTJ': 'btn-blue',
  'INTP': 'btn-green',
  'ISFJ': 'btn-yellow',
  'ISFP': 'btn-red',
  'ISTJ': 'btn-yellow',
  'ISTP': 'btn-green',
}

/**
 * Set the bootstrap class for the color corresponding to the
 * auxiliary function for each four letter type
 */
seeourminds.bootstrap_class_for_aux = {
  'ENFJ': 'btn-blue',
  'ENFP': 'btn-red',
  'ENTJ': 'btn-blue',
  'ENTP': 'btn-green',
  'ESFJ': 'btn-yellow',
  'ESFP': 'btn-red',
  'ESTJ': 'btn-yellow',
  'ESTP': 'btn-green',
  'INFJ': 'btn-red',
  'INFP': 'btn-blue',
  'INTJ': 'btn-green',
  'INTP': 'btn-blue',
  'ISFJ': 'btn-red',
  'ISFP': 'btn-yellow',
  'ISTJ': 'btn-green',
  'ISTP': 'btn-yellow',
}
