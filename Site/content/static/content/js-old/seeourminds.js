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
  'ENFJ': 'btn-danger',
  'ENFP': 'btn-primary',
  'ENTJ': 'btn-success',
  'ENTP': 'btn-primary',
  'ESFJ': 'btn-danger',
  'ESFP': 'btn-warning',
  'ESTJ': 'btn-success',
  'ESTP': 'btn-warning',
  'INFJ': 'btn-primary',
  'INFP': 'btn-danger',
  'INTJ': 'btn-primary',
  'INTP': 'btn-success',
  'ISFJ': 'btn-warning',
  'ISFP': 'btn-danger',
  'ISTJ': 'btn-warning',
  'ISTP': 'btn-success',
}

/**
 * Set the bootstrap class for the color corresponding to the
 * auxiliary function for each four letter type
 */
seeourminds.bootstrap_class_for_aux = {
  'ENFJ': 'btn-primary',
  'ENFP': 'btn-danger',
  'ENTJ': 'btn-primary',
  'ENTP': 'btn-success',
  'ESFJ': 'btn-warning',
  'ESFP': 'btn-danger',
  'ESTJ': 'btn-warning',
  'ESTP': 'btn-success',
  'INFJ': 'btn-danger',
  'INFP': 'btn-primary',
  'INTJ': 'btn-success',
  'INTP': 'btn-primary',
  'ISFJ': 'btn-danger',
  'ISFP': 'btn-warning',
  'ISTJ': 'btn-success',
  'ISTP': 'btn-warning',
}
