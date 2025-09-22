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
          mapToRadix: ['.']
        }
      }
    });
  });

  // Máscara para área (CÓDIGO ALTERADO)
  const areaInputs = document.querySelectorAll('.area');
  areaInputs.forEach(input => {
    IMask(input, {
      mask: 'num m²', // Define um padrão: número seguido por " m²"
      blocks: {
        num: {
          mask: Number,
          thousandsSeparator: '.'
        }
      }
    });
  });
});