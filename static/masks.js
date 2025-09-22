document.addEventListener("DOMContentLoaded", () => {
  // Máscara de dinheiro
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

  // Máscara para área (ex: 180m²)
  const areaInputs = document.querySelectorAll('.area');
  areaInputs.forEach(input => {
    IMask(input, {
      mask: Number,
      min: 0,
      max: 10000,        // limite máximo de metros quadrados
      thousandsSeparator: '.',
      suffix:'m²',       // adiciona "m²" no final
      radix: ','
    });
  });
});
