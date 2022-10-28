function calcular_margen(){
   var  p_v_u = parseFloat(document.getElementById('p_v_u').value);
   var  c_v_u = parseFloat(document.getElementById('c_v_u').value);
   margen_pesos = p_v_u - c_v_u;
   margen_porcentaje = (margen_pesos/p_v_u)*100;

   alert('El margen de contribución es de '+margen_pesos + 'en pesos y de '+margen_porcentaje+ 'en procentaje');

}

function margen_pesos(p_v_u, c_v_u){
   margen_pesos = p_v_u - c_v_u;
   alert('El margen de contribución en pesos'+margen_pesos );
}

function margen_porcentaje(p_v_u, c_v_u){

   margen_pesos = p_v_u - c_v_u;
   margen_porcentaje = (margen_pesos/p_v_u)*100;

   alert('El margen de contribución en porcentaje es del'+margen_porcentaje+"%");

}
