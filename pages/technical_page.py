import streamlit as st

def technical_page_body():
    st.write("### Technical")
    st.info("Linear Regression Model")
    code = '''
        from sklearn.linear_model import LinearRegression
        linear_reg = LinearRegression()
        linear_reg.fit(X, y.values)
        y_pred = linear_reg.predict(X)
        from sklearn.metrics import mean_squared_error, mean_absolute_error
        import numpy as np
        error = np.sqrt(mean_squared_error(y, y_pred))
        print("${:,.02f}".format(error))
        result = $45,121.92
        '''
    st.code(code, language="python")

    st.info("Logistic Regression Model")
    code = '''
        from sklearn import preprocessing
        scaler = preprocessing.StandardScaler().fit(X)
        X_scaled = scaler.transform(X)
        X_scaled
        from sklearn.linear_model import LogisticRegression
        log_reg = LogisticRegression(random_state=0)
        log_reg.fit(X_scaled, y.values)
        y_pred = log_reg.predict(X_scaled)
        error = np.sqrt(mean_squared_error(y, y_pred))
        print("${:,.02f}".format(error))
        result = $45,980.36
        '''
    st.code(code, language="python")

    st.info("Decision Tree Regressor Model")
    code = '''
        from sklearn.tree import DecisionTreeRegressor
        dec_tree_reg = DecisionTreeRegressor(random_state=0)
        dec_tree_reg.fit(X, y.values)
        y_pred = dec_tree_reg.predict(X)
        error = np.sqrt(mean_squared_error(y, y_pred))
        print("${:,.02f}".format(error))
        results = $29,983.82
        '''
    st.code(code, language="python")

    st.info("Random Forest Regressor Model")
    code = '''
        from sklearn.ensemble import RandomForestRegressor
        rand_forest_reg = RandomForestRegressor(random_state=0)
        rand_forest_reg.fit(X, y.values)
        y_pred = rand_forest_reg.predict(X)
        error = np.sqrt(mean_squared_error(y, y_pred))
        print("${:,.02f}".format(error))
        result = $30,212.42
        '''
    st.code(code, language="python")

    st.info("Grid Search with Cross Validation")
    code = '''
        from sklearn.model_selection import GridSearchCV
        max_depth = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        parameters = {"max_depth": max_depth}

        regressor = DecisionTreeRegressor(random_state=0)
        gs = GridSearchCV(regressor, parameters, scoring='neg_mean_squared_error')
        gs.fit(X, y.values)
        #Best estimator model = Decision Tree Regressor with a max depth of 10.
        regressor = gs.best_estimator_

        regressor.fit(X, y.values)
        y_pred = regressor.predict(X)
        error = np.sqrt(mean_squared_error(y, y_pred))
        print("${:,.02f}".format(error))
        result = $32,430.91
        '''
    st.code(code, language="python")

    st.success(
        f"We use the Decision Tree Regressor as it gave us the lowest deviation "
        f"and apply the variables from the GSCV and then use that model for our "
        f"prediction app.")