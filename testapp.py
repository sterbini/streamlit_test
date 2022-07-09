import streamlit as st
import glob

aux=glob.glob('/eos/user/s/sterbini/*')
st.write(aux[2])

st.write('Hello, world!!')
x = st.slider('x')
st.write(x, 'squared is', x * x)

if st.checkbox('test'):
        st.success('Passed')
else:
        st.warning('Failed')


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

import plotly.figure_factory as ff
import numpy as np

@st.cache
def plotMe():
        # Add histogram data
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        # Group data together
        hist_data = [x1, x2, x3]

        group_labels = ['Group 1', 'Group 2', 'Group 3']

        # Create distplot with custom bin_size
        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])

        return fig

st.plotly_chart(plotMe(), use_container_width=True)
st.sidebar.markdown('# Title')
answer=st.sidebar.radio('ssa',['Test','Test2','Test3'])

if answer=='Test':
        st.write('Guido')
