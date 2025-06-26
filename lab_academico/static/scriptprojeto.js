document.getElementById('form-project').addEventListener('submit', e => {
  console.log('Submit disparado!');
});

document.addEventListener('DOMContentLoaded', function() {
    const addBtn = document.getElementById('add-participant-btn');
    const participantsContainer = document.getElementById('participants-container');

    addBtn.addEventListener('click', function() {
        const participantDiv = document.createElement('div');
        participantDiv.className = 'participant';

        participantDiv.innerHTML = `
            <div class="input-box">
                <label class="form-label">Nome do Participante</label>
                <input type="text" name="participant_name[]" placeholder="Digite o nome" class="form-control" required>
            </div>
            <div class="input-box">
                <label class="form-label">Função</label>
                <select name="participant_role[]" class="form-control" required>
                    <option value="" disabled selected>Selecione a função</option>
                    <option value="Desenvolvedor">Desenvolvedor</option>
                    <option value="Cliente">Cliente</option>
                </select>
            </div>
        `;

        participantsContainer.appendChild(participantDiv);
    });

    const statusSelect = document.getElementById('project-status');
    const endDateContainer = document.getElementById('end-date-container');

    statusSelect.addEventListener('change', function() {
        if (this.value === 'finalizado') {
            endDateContainer.style.display = 'block';
            const endDateInput = document.getElementById('project-end-date');
            const today = new Date().toISOString().split('T')[0];
            endDateInput.value = today;
            endDateInput.min = today;
        } else {
            endDateContainer.style.display = 'none';
        }
    });
});
