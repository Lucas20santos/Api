import './App.css';

function App() {
  return (
    <div className="login">
      <div className='elipse'>
        <div className='text'>
          <p>Acesso de Controle</p>
        </div>
      </div>

      <div className='form'>
        <form>
          <input type="text" name="cpf" value="CPF"></input>
          <input type="password" name="senha" value="senha"></input>
          <input type="submit" name="enviar" value="Enviar"></input>
        </form>
      </div>

    </div>
  );
}

export default App;
