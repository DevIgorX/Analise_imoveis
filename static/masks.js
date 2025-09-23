document.addEventListener("DOMContentLoaded", () => {
  // Máscara de dinheiro (sem alterações)
  const moneyInputs = document.querySelectorAll('.money');
  moneyInputs.forEach(input => {
    IMask(input, {
      mask: 'R$ num',
      blocks: {
        num: {
          mask: Number,
          thousandsSeparator: '.',
          radix: ',',
          scale: 2,
          padFractionalZeros: true,
          normalizeZeros: true,
          mapToRadix: ['.']
        }
      }
    });
  });


// --- Máscara de Área em JavaScript Puro ---
const areaInputs = document.querySelectorAll('.area');

areaInputs.forEach(function(input) {
  input.addEventListener('input', function(e) {
    // Pega o valor atual e remove tudo que não for número
    let value = e.target.value.replace(/\D/g, '');
    
    if (value.length > 0) {
      // Formata o valor com o sufixo "m²"
      e.target.value = value + 'm²';
      
      // Reposiciona o cursor para antes do "m²"
      // Isso permite que o usuário continue digitando o número
      e.target.setSelectionRange(value.length, value.length);
    }
  });

  // Garante que se o usuário clicar no meio, o cursor vá para a posição correta
  input.addEventListener('click', function(e) {
      let numericValue = e.target.value.replace(/\D/g, '');
      e.target.setSelectionRange(numericValue.length, numericValue.length);
  });
});
});